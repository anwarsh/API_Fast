from django.contrib import admin

# Register your models here.


from .models import SystemResponse, Conversation , TroubleshootingTicket
# Register your models here.

admin.site.register(SystemResponse)
admin.site.register(Conversation)
admin.site.register(TroubleshootingTicket)
