from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class TroubleshootingTicket(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Conversation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(TroubleshootingTicket, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class SystemResponse(models.Model):
    ticket = models.ForeignKey(TroubleshootingTicket, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
