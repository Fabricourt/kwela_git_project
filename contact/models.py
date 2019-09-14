from django.db import models
from datetime import datetime
from realtors.models import Realtor
from ckeditor.fields import RichTextField
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    name = models.ForeignKey(User, on_delete= models.CASCADE,blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    header = models.CharField(max_length=300, blank=True, null=True )
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f' Names// {self.name.first_name}-{self.name.last_name} --Desc//  {self.name.header} --Email//  {self.email}-- Phone//  {self.phone} '
 


class Sema(models.Model):
  listing = models.CharField(max_length=200)
  listing_id = models.IntegerField()
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)
  contact_date = models.DateTimeField(default=datetime.now, blank=True)
  user_id = models.IntegerField(blank=True)
  def __str__(self):
    return self.name

