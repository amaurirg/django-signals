from django.contrib.auth.models import User
from django.db.models.signals import post_save

from exemplo_signals.models import Profile


def cria_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(usuario=instance)
    elif not hasattr(instance, 'profile'):
        Profile.objects.create(usuario=instance)


post_save.connect(cria_profile, sender=User)
