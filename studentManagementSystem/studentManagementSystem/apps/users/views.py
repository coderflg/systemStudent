from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from . import serializer
from . import models


# Create your views here.
class UserLogin(GenericAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

    def post(self, request):
        data = request.data.get("form")
        username, password = data.get("username"), data.get("password")
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return Response("error")
        # ser = serializer.UserSerializer(user)
        ser = self.get_serializer(user)
        print(ser.data)
        return Response(ser.data)


class UserRegister(GenericAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserSerializer

    def post(self, request):
        data = request.data
        print(data.get("form"))
        try:
            ser = self.get_serializer(data=data.get("form"))
            ser.is_valid()
            user = ser.save()
        except:
            return Response("failed")
        serRes = self.get_serializer(user)
        return Response(serRes.data)


class Check(APIView):
    def get(self, requests, pk):
        query = requests.query_params
        if str(pk) == "1":
            try:
                models.User.objects.get(mobile=query.get("check"))
            except:
                return Response("success")
            return Response("exists")
        if str(pk) == "2":
            try:
                models.User.objects.get(nickname=query.get("check"))
            except:
                return Response("success")
            return Response("exists")
        if str(pk) == "3":
            try:
                models.User.objects.get(username=query.get("check"))
            except:
                return Response("success")
            return Response("exists")


