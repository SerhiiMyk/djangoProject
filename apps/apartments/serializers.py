from rest_framework.serializers import ModelSerializer

from .models import ApartmentsModel


class ApartmentSerializer(ModelSerializer):
    class Meta:
        model = ApartmentsModel
        exclude = ('profile',)

        # extra_kwargs = {
        #     'users': {'read_only': True}
        # }


class ApartmentPhotoSerializer(ModelSerializer):
    class Meta:
        model = ApartmentsModel
        fields = ('photo',)
