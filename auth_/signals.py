from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from auth_.models import MainUser, Profile
from rest_framework.authtoken.models import Token
import logging
from password_manager.models import WebSitePassword, PasswordCollection

logging.basicConfig(
    level=logging.INFO,
    filename='out.log',
    filemode='a',
    format='%(asctime)s -- %(levelname)s:%(levelno)s -- %(message)s',
)


@receiver(post_save, sender=MainUser)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, country='KZ')


@receiver(post_save, sender=WebSitePassword)
def website_password_created(sender, instance, created, **kwargs):
    if created:
        if not instance.collection:
            instance.collection = PasswordCollection.objects.get(id=1)


@receiver(post_save, sender=Token)
def token_created(sender, instance, created, **kwargs):
    if created:
        logging.info('token created')


@receiver(post_delete, sender=Token)
def token_created(sender, instance, **kwargs):
    logging.info('token deleted')
