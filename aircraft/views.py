from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import AircraftModel
from .serializers import AircraftSerializer


class AircraftReadCreateView(APIView):
    def get(self, *args, **kwargs):
        year = self.request.query_params.get('year')
        aircrafts = AircraftModel.objects.all()
        if year:
            aircrafts = AircraftModel.objects.filter(year=year)
        serializer = AircraftSerializer(instance=aircrafts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AircraftSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class AircraftRetriveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AircraftModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('aircraft with this id is not found', status.HTTP_404_NOT_FOUND)
        aircraft = AircraftModel.objects.get(pk=pk)
        serializer = AircraftSerializer(instance=aircraft)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = AircraftModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('aircraft with this id is not found', status.HTTP_404_NOT_FOUND)
        aircraft = AircraftModel.objects.get(pk=pk)
        serializer = AircraftSerializer(instance=aircraft, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = AircraftModel.objects.get(pk=pk)
        if not exists:
            return Response('aircraft with this id is not found', status.HTTP_404_NOT_FOUND)
        aircraft = AircraftModel.objects.get(pk=pk)
        aircraft.delete()
        return Response(status.HTTP_204_NO_CONTENT)

# class AircraftRetriveByYearView(APIView):
#     def get(self, *args, **kwargs):
#         year = kwargs.get('year')
#         exists = AircraftModel.objects.filter(year=2000).exists()
#         if not exists:
#             return Response([], 'aircraft with this year is not found', status.HTTP_404_NOT_FOUND)
#         aircraft = AircraftModel.objects.filter(year=2000)
#         serializer = AircraftSerializer(instance=aircraft, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
