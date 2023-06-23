from django.contrib.auth import authenticate
from django.utils import timezone

from drf_spectacular.utils import extend_schema

from rest_framework import status, generics, exceptions, response
from .serializers import LoginSerializer, UserSerializer, UserTokenSerializer

from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(generics.GenericAPIView):
    """ Login view return user data and jwt tokens """
    authentication_classes = ()
    permission_classes = ()
    serializer_class = LoginSerializer

    @extend_schema(
        request=LoginSerializer,
        responses={
            status.HTTP_200_OK: UserTokenSerializer()
        },
        summary='Login endpoint',
        description='Login user and return user data with tokens.'
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid()
        user = authenticate(**serializer.validated_data)
        if not user:
            raise exceptions.AuthenticationFailed()
        user.last_login = timezone.now()
        user.save()

        refresh = RefreshToken.for_user(user)
        data = {
            "user": UserSerializer(instance=user, context={"request": request}).data,
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return response.Response(data=data, status=status.HTTP_200_OK)
