from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import ComputerModel


class ComputerReadCreateView(APIView):
    def get(self, *args, **kwargs):
        computers = ComputerModel.objects.all().values()
        return Response(computers, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        computer = ComputerModel.objects.create(**data)
        return Response(model_to_dict(computer), status.HTTP_201_CREATED)


class ComputerRetriveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('computer with this id is not found', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        return Response(model_to_dict(computer), status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = ComputerModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('computer with this id is not found', status.HTTP_404_NOT_FOUND)
        ComputerModel.objects.filter(pk=pk).update(**data)
        return Response('car updated', status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = ComputerModel.objects.get(pk=pk)
        if not exists:
            return Response('computer with this id is not found', status.HTTP_404_NOT_FOUND)
        computer = ComputerModel.objects.get(pk=pk)
        computer.delete()
        return Response(status.HTTP_204_NO_CONTENT)