from django.db import models
from datetime import datetime


# Create your models here.
class Pic(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    name = models.CharField(max_length=32)
    time = models.DateTimeField(default=datetime.now)


#class Meta:
   # db_table = ""
