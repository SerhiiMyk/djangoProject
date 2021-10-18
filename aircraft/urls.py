from django.urls import path
from aircraft.views import AircraftReadCreateView, AircraftRetriveUpdateDestroyView, AircraftRetriveByYearView

urlpatterns = [
    path('', AircraftReadCreateView.as_view()),
    path('/<int:pk>', AircraftRetriveUpdateDestroyView.as_view()),
    path('?year=<int:year>', AircraftRetriveByYearView.as_view())
]
