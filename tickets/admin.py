from django.contrib import admin
from .models import Client, Reservation , Film
# Register your models here.

admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(Film)