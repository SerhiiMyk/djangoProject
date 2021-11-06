from django.urls import path

from apps.apartments.views import ApartmentListCreateView, ApartmentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', ApartmentListCreateView.as_view()),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyAPIView.as_view()),
]
