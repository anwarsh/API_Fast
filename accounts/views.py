from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TroubleshootingTicket, Conversation, SystemResponse
from .serializers import TroubleshootingTicketSerializer, ConversationSerializer, SystemResponseSerializer

class TroubleshootingTicketListCreateAPIView(APIView):
    def get(self, request):
        tickets = TroubleshootingTicket.objects.all()
        serializer = TroubleshootingTicketSerializer(tickets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TroubleshootingTicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ConversationListCreateAPIView(APIView):
    def get(self, request):
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ConversationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SystemResponseListCreateAPIView(APIView):
    def get(self, request):
        responses = SystemResponse.objects.all()
        serializer = SystemResponseSerializer(responses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SystemResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
