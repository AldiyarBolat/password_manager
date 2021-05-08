from django.contrib import admin
from password_manager.models import PasswordCollection, WebSitePassword, WifiPassword, WebSiteBookmark

admin.site.register(PasswordCollection)
admin.site.register(WebSitePassword)
admin.site.register(WifiPassword)
admin.site.register(WebSiteBookmark)
