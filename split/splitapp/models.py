from django.db import models
import datetime

# Create your models here.
class User(models.Model):
  time=models.DateTimeField('time requested')
  name=models.CharField(max_length=50)
  phone=models.PositiveIntegerField()
  def __str__(self):
    return self.time+self.name+self.phone
  #returns true if the time has already passed
  def checkExpired(self):
    return datetime.datetime.now()>=time
