# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..users.permissions import IsActive
from ..users.serisalizers import UserSerializer
from .filters import ApartmentFilter
from .models import ApartmentsModel
from .serializers import ApartmentPhotoSerializer, ApartmentSerializer


class ApartmentListView(ListCreateAPIView):
    serializer_class = ApartmentSerializer
    queryset = ApartmentsModel.objects.all()
    permission_classes = (AllowAny,)
    filterset_class = ApartmentFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return AllowAny(),
        return IsActive(),


class ApartmentCreateView(GenericAPIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        print(data)
        serializer = ApartmentSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        profile = self.request.user.profile
        print(profile)
        serializer.save(profile=self.request.user.profile)
        user = UserSerializer(self.request.user).data
        return Response(user, status.HTTP_200_OK)


class ApartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentsModel.objects.all()
    serializer_class = ApartmentSerializer


class AddApartmentPhotoView(UpdateAPIView):
    serializer_class = ApartmentPhotoSerializer

    def get_object(self):
        return self.request.user.apartments
