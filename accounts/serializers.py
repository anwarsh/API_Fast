from rest_framework import serializers
from .models import TroubleshootingTicket, Conversation, SystemResponse

class TroubleshootingTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TroubleshootingTicket
        fields = ['id', 'title', 'description', 'status', 'created_at']

class ConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'user', 'ticket', 'text', 'timestamp']

class SystemResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemResponse
        fields = ['id', 'ticket', 'text', 'timestamp']
