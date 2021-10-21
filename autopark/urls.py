from django.urls import path
from .views import AutoParkListView, AutoParkAddCar, AutoParkRetrieveDestroyAPIView

urlpatterns = [
    path('', AutoParkListView.as_view()),
    path('/<int:pk>', AutoParkRetrieveDestroyAPIView.as_view()),
    path('/<int:pk>/add_car', AutoParkAddCar.as_view())
]
