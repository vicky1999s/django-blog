from django.db.models.signals import post_save
from .models import profile
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)

@receiver(signal=post_save, sender=User)
def create_profile(sender, instance, **kwargs):
        instance.profile.save()