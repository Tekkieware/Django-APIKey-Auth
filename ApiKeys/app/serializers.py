from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from rest_framework import serializers




class UserSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = User
        fields = ['__all__']



class MyTokenObtainPairSeriaizer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'username', 'last_name', 'email', 'token', 'password']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)