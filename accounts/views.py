from rest_framework import viewsets , permissions
from .models import TroubleshootingTicket, Conversation, SystemResponse
from .serializers import TroubleshootingTicketSerializer, ConversationSerializer, SystemResponseSerializer
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class TroubleshootingTicketViewSet(viewsets.ModelViewSet):
    queryset = TroubleshootingTicket.objects.all()
    serializer_class = TroubleshootingTicketSerializer
    permission_classes = [permissions.IsAuthenticated]

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

class SystemResponseViewSet(viewsets.ModelViewSet):
    queryset = SystemResponse.objects.all()
    serializer_class = SystemResponseSerializer
    permission_classes = [permissions.IsAuthenticated]
