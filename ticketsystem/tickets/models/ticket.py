from django.db import models

class Ticket(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    allocation = models.IntegerField(min=0)