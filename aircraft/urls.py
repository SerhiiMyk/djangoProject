from django.urls import path
from aircraft.views import AircraftReadCreateView, AircraftRetriveUpdateDestroyView

urlpatterns = [
    path('', AircraftReadCreateView.as_view()),
    path('/<int:pk>', AircraftRetriveUpdateDestroyView.as_view()),
]
