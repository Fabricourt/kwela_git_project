from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
import uuid  # Required for unique book instances
from datetime import date
from datetime import datetime
from django.urls import reverse
from realtors.models import Realtor
from clients.models import Client


from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.


class Plot_size(models.Model):
    size = models.CharField(max_length=100)

    def __str__(self):
        return self.size

class Plot_type(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.type




class Plot(models.Model):
    """Model representing a plot (but not a specific plot)."""
    title = models.CharField(max_length=200, blank=False, null=True)
    plotnumber = models.CharField(max_length=200, blank=False, null=True)
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING,  blank=True, null=True, help_text='optional')
    location = models.CharField(max_length=200, blank=False, null=True)
    history = RichTextField(max_length=1000, blank=True, null=True)
    price = models.IntegerField()
    plot_type =  models.ForeignKey(Plot_type, on_delete=models.DO_NOTHING,  blank=False, null=True)
    plot_size =  models.ForeignKey(Plot_size, on_delete=models.DO_NOTHING,  blank=False, null=True)
    photo_map = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(blank=True, null=True)
    def __int__(self):
        """String for representing the Model object."""
        return self.title


