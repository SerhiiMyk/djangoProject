from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from ..profile.serializers import AvatarSerializer
from .permissions import IsStaff, IsSuperUser
from .serisalizers import UserSerializer

UserModel: User = get_user_model()


class UserListView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return AllowAny(),
        return IsAuthenticated(),

    def get_queryset(self):
        return UserModel.objects.exclude(id=self.request.user.id)

    def get_serializer_context(self):
        return {'request': self.request}


class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()


class UserToActiveView(GenericAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsStaff,)

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
    permission_classes = (IsSuperUser,)

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


class AddAvatarView(GenericAPIView):

    def patch(self, *args, **kwargs):
        avatar_data = self.request.FILES.get('avatar')
        serializer = AvatarSerializer(data={'url': avatar_data})
        serializer.is_valid(raise_exception=True)
        serializer.save(profile=self.request.user.profile)
        user = UserSerializer(self.request.user).data
        return Response(user, status.HTTP_200_OK)
