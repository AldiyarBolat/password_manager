from django.urls import path
from rest_framework import routers

from .views import (
    create_password_collection,
    PasswordCollectionListAPIView,
    PasswordCollectionAPIView,
    WebSitePasswordListAPIView,
    WebSitePasswordViewSet,
    WifiPasswordViewSet,
    WebSiteBookmarkViewSet,
)


router = routers.SimpleRouter()
router.register('website_password', WebSitePasswordViewSet, basename='website_password')
router.register('wifi_password', WifiPasswordViewSet, basename='wifi_password')
router.register('website_bookmark', WebSiteBookmarkViewSet, basename='website_bookmark')

urlpatterns = [
    path('create_password_collection', create_password_collection),
    path('password_collections_list', PasswordCollectionListAPIView.as_view()),
    path('password_collection/<int:pk>/', PasswordCollectionAPIView.as_view()),

    path('website_password_list', WebSitePasswordListAPIView.as_view()),
] + router.urls
