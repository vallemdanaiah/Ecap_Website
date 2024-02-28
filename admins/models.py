from django.db import models

# Create your models here.
class StdDetailes(models.Model):
    stdname = models.CharField(max_length=100)
    stdcourse = models.CharField(max_length=100)
    stdbranch = models.CharField(max_length=100)
    stdjoining = models.DateTimeField()
    stdvillage = models.CharField(max_length=100)
    stdmcetrank = models.IntegerField()
    stdemail = models.EmailField()
    stdphoto = models.ImageField(upload_to='media/')
    