# Generated by Django 2.2.5 on 2021-05-03 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('password_manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebSiteBookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка на закладку')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='password_manager.PasswordCollection', verbose_name='Коллекция')),
                ('website_password', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='password_manager.WifiPassword')),
            ],
            options={
                'verbose_name': 'Закладка от вебсайта',
                'verbose_name_plural': 'Закладки от вебсайтов',
            },
        ),
    ]
