from django.db import models
import datetime
from django.views.generic.dates import DateMixin

# Create your models here.
class UseName(models.Model):
    user_Name = models.CharField(max_length=60, unique=True)
    pas = models.CharField(max_length=50)

    def __str__(self):
        return self.user_Name + " " + self.pas

class AccessData(models.Model):
    user = models.CharField(max_length=60)
    item = models.CharField(max_length=75)
    date = models.DateField()
    endDate = models.DateField(True, default=0)

    def __str__(self):
        return str(self.date) + " " + self.item + " " + self.user + " " + str(self.endDate)