from django.db import models
import uuid  # Required for unique book instances
from datetime import date
from datetime import datetime
from django.urls import reverse
from clients.models import Client
from plotz.models import Plot


from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Payment(models.Model):
    """Model representing a plot (but not a specific plot)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular plot in the system")
    plot_number = models.ForeignKey(Plot,  on_delete= models.CASCADE,  blank=True, null=True, help_text='optional')
    client = models.ForeignKey(Client,  on_delete= models.CASCADE,  blank=True, null=True, help_text='optional')
    reciept_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    reciept_number =  models.CharField(null=True, blank=True, max_length=200)
    previous_balance = models.IntegerField()
    amount_paid =  models.CharField(null=True, blank=True, max_length=200)
    current_balance = models.IntegerField()
    is_published = models.BooleanField(default=True)
    reciept_date = models.DateTimeField(blank=True, null=True)
    entry_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        """String for representing the Model object."""
        return self.client.first_name