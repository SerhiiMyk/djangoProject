from django.urls import path

from apps.apartments.views import (
    AddApartmentPhotoView,
    ApartmentCreateView,
    ApartmentListView,
    ApartmentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('', ApartmentListView.as_view()),
    path('/create', ApartmentCreateView.as_view()),
    path('/<int:pk>', ApartmentRetrieveUpdateDestroyAPIView.as_view()),
    path('/add_photo', AddApartmentPhotoView.as_view())
]
