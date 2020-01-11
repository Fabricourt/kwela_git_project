from django.db import models
from datetime import datetime



from ckeditor.fields import RichTextField

class Realtor(models.Model):
  first_name = models.CharField(max_length=100, blank=True, null=True)
  last_name = models.CharField(max_length=100, blank=True, null=True)
  photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
  about_realtor = RichTextField(blank=True, null=True)
  phone_1 = models.CharField(max_length=20, blank=True, null=True)
  whatsapp_phone = models.CharField(max_length=100, blank=True, null=True)
  email = models.CharField(max_length=50, blank=True, null=True)
  facebook = models.CharField(max_length=100, blank=True, null=True)
  twitter = models.CharField(max_length=100, blank=True, null=True)
  website = models.CharField(max_length=100, blank=True, null=True)
  instagram = models.CharField(max_length=100, blank=True, null=True)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.first_name
 