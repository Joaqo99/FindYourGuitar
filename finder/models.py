from django.db import models
from list_tracker.models import List


class Status(models.Model):
    status_name = models.CharField(max_length=50, null=True)
    status_id = models.BigAutoField(primary_key=True)

    def __str__(self):
        return self.status_name
class Search(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    articles = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id) + " - " + str(self.date_time)
class Guitar(models.Model):
    g_list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)
    search = models.ForeignKey(Search, on_delete=models.CASCADE, null=True)
    brand = models.CharField(max_length=250, null=True)
    g_model = models.CharField(max_length=250, null=True)
    title = models.CharField(max_length=250, null=True)
    #description = models.TextField(max_length=2000, null=True)
    link = models.CharField(max_length=1000, null=True)
    price = models.CharField(max_length=10, null=True)

    def __str__(self):
        return f'{self.brand} {self.g_model} --- ID: {self.id}'

