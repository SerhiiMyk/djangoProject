from apps.cars.serializers import CarSerializer
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import AllowAny

from .models import AutoParkModel
from .serializers import AutoParkSerializers


# Create your views here.
class AutoParkListView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializers
    # permission_classes = (AllowAny,)


class AutoParkRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializers


class AutoParkAddCar(CreateAPIView):
    serializer_class = CarSerializer
    queryset = AutoParkModel.objects.all()


    def perform_create(self, serializer):
        autopark = self.get_object()
        serializer.save(autopark=autopark)
        super().perform_create(serializer)
