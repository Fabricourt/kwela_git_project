from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Wasifu


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Wasifu.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_Wasifu(sender, instance, **kwargs):
    instance.wasifu.save()
