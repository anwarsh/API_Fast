from django.contrib import admin

# Register your models here.

from rest_framework.authtoken.models import Token

from .models import SystemResponse, Conversation , TroubleshootingTicket
# Register your models here.

admin.site.register(SystemResponse)
admin.site.register(Conversation)
admin.site.register(TroubleshootingTicket)


