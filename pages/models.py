from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime


class Photoi(models.Model):
  title = models.CharField(max_length=50, blank=True, null=True)
  photo_logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_header = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_footer= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
 
  def __str__(self):
    return self.title



class Photoa(models.Model):
  title = models.CharField(max_length=50, blank=True, null=True)
  photo_logo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_header = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_page = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_footer= models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
 
  def __str__(self):
    return self.title