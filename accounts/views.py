from rest_framework import viewsets
from .models import TroubleshootingTicket, Conversation, SystemResponse
from .serializers import TroubleshootingTicketSerializer, ConversationSerializer, SystemResponseSerializer

class TroubleshootingTicketViewSet(viewsets.ModelViewSet):
    queryset = TroubleshootingTicket.objects.all()
    serializer_class = TroubleshootingTicketSerializer

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

class SystemResponseViewSet(viewsets.ModelViewSet):
    queryset = SystemResponse.objects.all()
    serializer_class = SystemResponseSerializer
