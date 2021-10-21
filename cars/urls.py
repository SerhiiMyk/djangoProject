from django.urls import path
from cars.views import CarListCreateView, CarRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyAPIView.as_view()),
]
