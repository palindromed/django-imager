from django.conf import settings
from .models import ImagerProfile
from django.db.models.signals import post_save
# import logging
from django.dispatch import receiver

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def post_save_receiver(sender, instance, created, **kwargs):
#     if created:
#         ImagerProfile.objects.create(user=instance)
#         print('does this work')
    # if kwargs.get(created, False):
    #     try:
    #         new_profile = ImagerProfile(user=kwargs[instance])
    #         new_profile.save()
    #     except (KeyError, ValueError):
    #         print('could not save')

# post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_for_new_user(sender, created, instance, **kwargs):
    if created:
        profile = ImagerProfile(user=instance)
        profile.save()
