import logging
from logging.handlers import RotatingFileHandler
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import LimitOffsetPagination

from .models import PasswordCollection, WebSitePassword, WifiPassword, WebSiteBookmark
from .serializers import (
	PasswordCollectionSerializer,
	PasswordCollectionsSerializer,
	WebSitePasswordSerializer,
	WifiPasswordSerializer,
	WebSiteBookmarkSerializer,
)


logging.basicConfig(
	level=logging.INFO,
	filename='out.log',
	filemode='a',
	format='%(asctime)s -- %(levelname)s:%(levelno)s -- %(message)s',
)


@api_view(['POST'])
def create_password_collection(request):
	serializer = PasswordCollectionSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save(created_by=request.user)
		return Response(serializer.data, status=status.HTTP_200_OK)
	return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PasswordCollectionListAPIView(APIView):
	def get(self, request):
		password_collections = PasswordCollection.objects.filter(created_by=request.user)
		serializer = PasswordCollectionsSerializer(password_collections, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class PasswordCollectionAPIView(APIView):
	def get(self, request, pk):
		password_collection = PasswordCollection.objects.get(id=pk, created_by=request.user)
		serializer = PasswordCollectionSerializer(password_collection)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def delete(self, request, pk):
		password_collection = PasswordCollection.objects.get(id=pk, created_by=request.user)
		password_collection.delete()
		return Response({'deleted': 'ok'}, status=status.HTTP_204_NO_CONTENT)


class WebSitePasswordListAPIView(APIView):
	def get(self, request):
		website_passwords = WebSitePassword.objects.filter(created_by=request.user)
		serializer = WebSitePasswordSerializer(website_passwords, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class WebSitePasswordViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = WebSitePassword.objects.all()
	serializer_class = WebSitePasswordSerializer
	pagination_class = LimitOffsetPagination

	def perform_create(self, serializer):
		serializer.save()
		logging.info(f'WebSitePassword created, ID: {serializer.instance}')


class WifiPasswordViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = WifiPassword.objects.all()
	serializer_class = WifiPasswordSerializer
	pagination_class = LimitOffsetPagination

	def perform_create(self, serializer):
		serializer.save()
		logging.info(f'WifiPassword created, ID: {serializer.instance}')


class WebSiteBookmarkViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthenticated,)
	queryset = WebSiteBookmark.objects.all()
	serializer_class = WebSiteBookmarkSerializer
	pagination_class = LimitOffsetPagination

	def perform_create(self, serializer):
		serializer.save()
		logging.info(f'Bookmark created, ID: {serializer.instance}')
