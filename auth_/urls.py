from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

from .views import create_user, AuthorizationAPIView, ProfileViewSet


router = routers.SimpleRouter()
router.register('profile', ProfileViewSet, basename='profile')


urlpatterns = [
    path('create_user', create_user),
    path('login/', AuthorizationAPIView.as_view()),
] + router.urls
