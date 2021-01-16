from django.db import models

# Create your models here.
class UseName(models.Model):
    user_Name = models.CharField(max_length=60, unique=True)
    pas = models.CharField(max_length=50)

    def __str__(self):
        return self.user_Name + " " + self.pas

class AccessData(models.Model):
    user = models.ForeignKey(UseName, on_delete=models.CASCADE)
    item = models.CharField(max_length=75)
    date = models.DateField()

    def __str__(self):
        return str(self.date) + self.item + self.user