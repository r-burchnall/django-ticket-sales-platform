from django.db import models

class Purchase(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    allocation = models.IntegerField(min=0)