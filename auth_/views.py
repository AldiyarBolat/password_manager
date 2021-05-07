# from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.db import IntegrityError
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from .models import MainUser as User, Profile
from .serializers import ProfileSerializer


@api_view(['POST'])
def create_user(request):
	try:
		user = User.objects.create_user(username=request.data.get('username'),
									    email=request.data.get('email'),
										password=request.data.get('password'))
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key}, status=status.HTTP_201_CREATED)
	except IntegrityError:
		return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class AuthorizationAPIView(APIView):
	permission_classes = (AllowAny,)

	def post(self, request):
		serializer = AuthTokenSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data.get('user')
		token, created = Token.objects.get_or_create(user=user)
		return Response({'token': token.key})

	def delete(self, request):
		request.auth.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class ProfileViewSet(viewsets.ModelViewSet):
	queryset = Profile.objects.all()
	serializer_class = ProfileSerializer
	parser_classes = [MultiPartParser, FormParser, JSONParser]

	@action(detail=False, methods=['POST'])
	def upload_photo(self, request, *args, **kwargs):
		profile = Profile.objects.get(user=request.user)
		profile.photo = request.data['image']
		profile.save()
		return Response(status=status.HTTP_200_OK)


