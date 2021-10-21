from rest_framework.serializers import ModelSerializer
from .models import AutoParkModel
from cars.serializers import CarSerializer


class AutoParkSerializers(ModelSerializer):
    cars = CarSerializer(many=True)

    class Meta:
        model = AutoParkModel
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)


