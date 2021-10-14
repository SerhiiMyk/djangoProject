from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response

from rest_framework.views import APIView
import json


class User(APIView):

    def get(self, *args, **kwargs):
        try:
            with open('users.json') as file:
                users = json.load(file)
            return Response(users)
        except Exception:
            return Response([])

    def post(self, *args, **kwargs):
        with open('users.json', 'r+') as file:
            users: list = json.load(file)
            file.seek(0)
            last_id = users[-1].get('id')
            users.append({"id":last_id+1,**self.request.data})
            json.dump(users, file)

        return Response('ok')
