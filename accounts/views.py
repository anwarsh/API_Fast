from rest_framework import viewsets , permissions
from .models import TroubleshootingTicket, Conversation, SystemResponse
from .serializers import TroubleshootingTicketSerializer, ConversationSerializer, SystemResponseSerializer
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class TroubleshootingTicketViewSet(viewsets.ModelViewSet):
    queryset = TroubleshootingTicket.objects.all()
    serializer_class = TroubleshootingTicketSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    

class SystemResponseViewSet(viewsets.ModelViewSet):
    queryset = SystemResponse.objects.all()
    serializer_class = SystemResponseSerializer
    
