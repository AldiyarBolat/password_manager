from django.contrib import admin
from auth_.models import MainUser, Profile

admin.site.register(MainUser)
admin.site.register(Profile)