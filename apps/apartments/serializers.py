from rest_framework.serializers import ModelSerializer

from .models import ApartmentsModel


class ApartmentSerializer(ModelSerializer):
    class Meta:
        model = ApartmentsModel
        fields = '__all__'
        # extra_kwargs = {
        #     'users': {'read_only': True}
        # }
