from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField 
from users .models import User
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.

class Bookspot(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.CharField(max_length=100, blank=True, null=True)
    approved = models.BooleanField(default=False, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)    
    is_published = models.BooleanField(default=True)
    def __str__(self):
        return f'Name--// {self.first_name}  Phone--// {self.phone_number}  id Number--// {self.id_number} Email--// {self.email} Booking_Time--// {self.timestamp} '
        
 
