from django.shortcuts import render
from rest_framework import viewsets
from SessionApp.models import SESSION
from .serializers import SessionSerialiazer# Create your views here.
class SessionViewSet(viewsets.ModelViewSet):
    queryset = SESSION.objects.all()
    serializer_class = SessionSerialiazer
    