from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serisalizers import UserSerializer

UserModel: User = get_user_model()


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAuthenticated(),


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserToActiveView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.acrive_on(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.acrive_off(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)


class UserToAdminView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def patch(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_admin(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        user = self.get_object()
        UserModel.objects.to_user(user)
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)
