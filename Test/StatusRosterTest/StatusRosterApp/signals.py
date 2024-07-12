from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Roster, Log
from django.utils import timezone

@receiver(post_save, sender=Roster)
def create_log(sender, instance, created, user=None, **kwargs):
    if created and user:
        Log.objects.create(member_id=user, roster_id=instance, timestamp=timezone.now())
