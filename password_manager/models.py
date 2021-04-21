from django.db import models


class PasswordCollection(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')

    class Meta:
        verbose_name = 'Коллекция Паролей'
        verbose_name_plural = 'Коллекций Паролей'


class BasePassword(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    collection = models.ForeignKey(PasswordCollection, on_delete=models.CASCADE, verbose_name='Коллекция')

    class Meta:
        abstract = True


class WebSitePassword(BasePassword):
    website = models.CharField(max_length=255, verbose_name='Веб сайт')
    login = models.CharField(max_length=100, verbose_name='Логин')

    class Meta:
        verbose_name = 'Пароль от вебсайта'
        verbose_name_plural = 'Пароли от вебсайта'


class WifiPassword(BasePassword):
    wifi_name = models.CharField(max_length=100, verbose_name='Логин')

    class Meta:
        verbose_name = 'Пароль от вайфай'
        verbose_name_plural = 'Пароли от вайфай'
