from django.db import models

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
class Guitar(models.Model):
    g_list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=250, null=True)
    g_model = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)
    description = models.TextField(max_length=2000, null=True)
    link = models.CharField(max_length=1000, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    def __str__(self):
        return f'{self.brand} {self.g_model} --- ID: {self.id}'