from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone

from datetime import timedelta

from badges.models import Pioneer


@receiver(user_logged_in, sender=User)
def check_1_year_birthday(sender, request, user, **kwargs):
    if (user.date_joined <= (timezone.now() - timedelta(days=365)) and not
       Pioneer.objects.filter(user=user).exists()):
        pioneer = Pioneer(user=user)
        pioneer.save()
