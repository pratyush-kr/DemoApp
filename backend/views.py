from django.shortcuts import render
from rest_framework import viewsets
from backend.models import User
from rest_framework.decorators import action
from backend.serializers import UserSerializer

# Create your views here.


class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    # @action(methods=["GET"], detail=False)
    # def get_user():
    #     # users = User.objects.all()
    #     return []