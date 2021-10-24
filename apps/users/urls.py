from django.urls import path

from .views import UserListView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', UserListView.as_view()),
    path('/<int:pk>', UserRetrieveUpdateDestroyAPIView.as_view()),
]