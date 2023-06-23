from rest_framework import serializers
from .models import Account


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            "email",
            "username",
            "first_name",
            "last_name",
            "middle_name",
            "phone",
            "avatar",
        ]


class UserTokenSerializer(serializers.Serializer):
    user = UserSerializer()
    refresh = serializers.CharField()
    access = serializers.CharField()


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False, allow_null=False)
    password = serializers.CharField(required=True, allow_blank=False, allow_null=False)


class LogoutSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True, allow_blank=False, allow_null=False)
