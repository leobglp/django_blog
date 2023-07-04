from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User) #When a User is saved the signal 'post_save' will be sent to receiver
def create_profile(sender, instance, created, **kwargs): #The receiver will run this function
    if created: #If user was created, create a profile
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User) #When a User is saved the signal 'post_save' will be sent to receiver
def save_profile(sender, instance, **kwargs): #The receiver will run this function
    instance.profile.save()