from rest_framework.serializers import ModelSerializer

from ..apartments.serializers import ApartmentSerializer
from .models import AvatarModel, ProfileModel


class AvatarSerializer(ModelSerializer):
    class Meta:
        model = AvatarModel
        fields = ('url',)


class ProfileSerializer(ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)
    avatars = AvatarSerializer(many=True, read_only=True)

    class Meta:
        model = ProfileModel
        exclude = ('user',)
