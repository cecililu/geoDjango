from datetime import datetime
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
import datetime


# Create your models here.

class Shapefile(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)
    file=models.FileField(upload_to='%Y/%M/%D')
    uploaded_data=models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.name