# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .filters import CarFilter
from .models import CarModel
from .serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)

    filterset_class = CarFilter

    # def get_queryset(self):
    #     year = self.request.query_params.get('year')
    #     auto_park_id = self.request.query_params.get('autoParkId')
    #     qs = CarModel.objects.all()
    #     if year:
    #         qs = qs.filter(year=year)
    #     if auto_park_id:
    #         qs = qs.filter(autopark_id=auto_park_id)
    #     return qs


class CarRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
