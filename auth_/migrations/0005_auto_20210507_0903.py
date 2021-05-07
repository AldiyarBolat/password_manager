# Generated by Django 2.2.5 on 2021-05-07 09:03

import auth_.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0004_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='avatars', validators=[auth_.validators.validate_name, auth_.validators.validate_size, auth_.validators.validate_extension]),
        ),
    ]
