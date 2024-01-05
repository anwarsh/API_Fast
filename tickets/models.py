from django.db import models 

#llll

class Film(models.Model):
    salle = models.CharField(max_length=50)
    film = models.CharField(max_length=50)
    date = models.DateField()

class Client(models.Model):
    nom = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)

class Reservation(models.Model):
    client = models.ForeignKey(Client, related_name ='reservation', on_delete = models.CASCADE)
    film = models.ForeignKey(Film, related_name = 'reservation',on_delete = models.CASCADE)