from django.db import models

from auth_.models import MainUser as User


class PasswordCollectionManager(models.Manager):
    def create_password_collection(self, name):
        return self.model(name).save()


class PasswordCollection(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = PasswordCollectionManager()

    class Meta:
        verbose_name = 'Коллекция Паролей'
        verbose_name_plural = 'Коллекций Паролей'


class BasePasswordManager(models.Manager):
    def create_base_password(self, name, description, password, collection, **extra_fields):
        return self.model(name, description, password, collection, **extra_fields).save()


class BasePassword(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    collection = models.ForeignKey(PasswordCollection, on_delete=models.CASCADE, verbose_name='Коллекция')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = BasePasswordManager()

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


class BaseBookmarkManager(models.Manager):
    def create_base_bookmark(self, name, **extra_fields):
        return self.model(name, **extra_fields).save()


class BaseBookmark(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    objects = BaseBookmarkManager()

    class Meta:
        abstract = True


class WebSiteBookmark(BasePassword):
    description = models.CharField(max_length=255, verbose_name='Описание')
    url = models.CharField(max_length=255, verbose_name='Ссылка на закладку')
    website_password = models.ForeignKey(WifiPassword, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Закладка от вебсайта'
        verbose_name_plural = 'Закладки от вебсайтов'
