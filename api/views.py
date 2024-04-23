from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Student, Contact
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class OneTOGet(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request: Request):
        user = request.user
        if user.is_authenticated:
            return Response({"status":200})
        