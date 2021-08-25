from django.db import models
#from finder.models import Guitar
# Create your models here.

class List(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name