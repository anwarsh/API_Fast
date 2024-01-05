from django.http import Http404, JsonResponse
from django.shortcuts import render
from .models import Client, Reservation, Film
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ClientSerialier, ReservationSerialier, FlimSerializer
from rest_framework import status , filters , generics , mixins
from rest_framework.views import APIView
# Create your views here.
# 1 without rest and no model query
def no_rest_no_model(request):

    guests = [
        {
            'id' : '1',
            'nom': 'anwar',
            'mobile':'0344433',
        },
        {
            'id':'2',
            'nom':'shaa',
            'mobile':'0304404',
        }
    ]
    return JsonResponse(guests, safe=False)


# 2 no rest from model,

def no_rest_from_model(request):
    data = Client.objects.all()
    response = {
        'clients':list(data.values('nom','mobile'))
    }
    return JsonResponse(response)

# 3 rest API fonction base views
# GET POST
@api_view(['GET','POST'])
def FBV_list(request):
    # GET 
    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerialier(client, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClientSerialier(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)


# GET PUT DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except client.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # GET
    if request.method == 'GET':
       serialiser = ClientSerialier(client)
       return Response(serialiser.data)
    # PUT
    if request.method == 'PUT':
       serialiser = ClientSerialier(client , data= request.data)
       if serialiser.is_valid():
           serialiser.save()
           return Response(serialiser.data)
       return Response(serialiser.error_messages , status= status.HTTP_404_NOT_FOUND)
    # DELETE 
    if request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# CBV class base views liste and create == GET and POST
class CBV_list(APIView):
    def get(self, request):
        client = Client.objects.all()
        serialiser = ClientSerialier(client, many=True)
        return Response(serialiser.data)
    def post(self,request):
        serializer =ClientSerialier(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_404_NOT_FOUND)

    
# CBV GET PUT DETELE
class CBV_pk(APIView):
    def get_object(self, pk):
        try:
            return Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            raise Http404 
        
    def get(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerialier(client)
        return Response(serializer.data)
    def put(self, request , pk):
        client = self.get_object(pk)
        serialiser = ClientSerialier(client , data= request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data, status=status.HTTP_201_CREATED)
        return Response(serialiser.data, status=status.HTTP_404_NOT_FOUND)
    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# Mixins list
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerialier

    def get(self , request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    
# Mixins GET PUT DETELE

class mixins_pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerialier

    def get(self, request,pk):
        return self.retrieve(request)
    def put(self, request, pk):
        return self.update(request)
    def delete(self, request, pk):
        return self.destroy(request)

class generics_list(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerialier



class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerialier


