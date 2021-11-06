# Create your views here.

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from .filters import ApartmentFilter
from .models import ApartmentsModel
from .serializers import ApartmentSerializer


class ApartmentListCreateView(ListCreateAPIView):
    serializer_class = ApartmentSerializer
    queryset = ApartmentsModel.objects.all()
    permission_classes = (AllowAny,)

    filterset_class = ApartmentFilter

class ApartmentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ApartmentsModel.objects.all()
    serializer_class = ApartmentSerializer
