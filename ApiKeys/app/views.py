from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import MyTokenObtainPairSeriaizer, UserSerializer, UserSerializerWithToken
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

@api_view(['POST'])
def registerUser(request):
    data = request.data

    user = User.objects.create(
        first_name=data['firstname'],
        last_name=data['lastname'],
        username=data['email'],
        email=data['email'],
        password=make_password(data['password'])
    )
    serializer = UserSerializerWithToken(user, many=False)
    
    return Response(serializer.data)
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSeriaizer