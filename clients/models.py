from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=True)
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    image = models.ImageField(default='default.jpg', upload_to='client_pics')
    phone = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.IntegerField(blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.last_name

    def save(self, **kwargs):
        super().save()
 

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
