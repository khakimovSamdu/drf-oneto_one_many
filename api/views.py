from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Student, Contact, Company, Product
from .serializers import StudentSerializers, ContactSerializers, CompanySerializers, ProductSerializers
from django.contrib.auth.models import User
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class OneTOGet(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request: Request, id=None, contact=None):
        user = request.user
        if user.is_authenticated:
            if id:
                try:
                    data = Student.objects.get(id=id)
                    serializer = StudentSerializers(data).data
                    return Response(serializer)
                except:
                    return Response({"ID error":f"Siz yuborgan {id} bazadan topilmadi"})
            elif contact:
                try:
                    data = Student.objects.get(contact = contact)
                    serializer = StudentSerializers(data).data
                    return Response(serializer)
                except:
                    return Response({"Contact id error":f"Siz yuborgan {contact} id Contact jadvlaidan topilmadi"})
                
            else:
                data = Student.objects.all()
                ruyxat = []
                for item in data:
                    serializer = StudentSerializers(item).data
                    ruyxat.append(serializer)
                return Response(ruyxat)
    
class OneToOneContact(APIView):
    authentication_classes = [BasicAuthentication]
    parser_classes = [IsAuthenticated]
    def get(self, request: Request, id=None):
        user = request.user
        if user.is_authenticated:
            if id:
                try:
                    data = Contact.objects.get(id=id)
                    serializers = ContactSerializers(data).data
                    return Response(serializers)
                except:
                    return Response({"ID error":f"Siz yuborgan {id} bazadan topilmadi"})
            else:
                data = Contact.objects.all()
                ruyxat = []
                for item in data:
                    serializers = ContactSerializers(item).data
                    ruyxat.append(serializers)
                return Response(ruyxat)
    def post(self, request: Request):
            serializers = ContactSerializers(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            return Response(serializers.errors)
    
class OnetoMenyCompany(APIView):
    authentication_classes=[BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request: Request, id=None):
        user = request.user
        if user.is_authenticated:
            if id:
                data = Company.objects.get(id=id)
                serializers = CompanySerializers(data).data
                return Response(serializers)
            else:
                ruyxat = []
                data = Company.objects.all()
                for item in data:
                    serializers = CompanySerializers(item).data
                    ruyxat.append(serializers)
                return Response(ruyxat)

class OnetoMenyProduct(APIView):
    authentication_classes = [BasicAuthentication]
    parser_classes = [IsAuthenticated]
    def get(self, request: Request, id=None):
        user = request.user
        if user.is_authenticated:
            if id:
                data = Product.objects.get(id=id)
                serializers = ProductSerializers(data).data
                return Response(serializers)
            else:
                data = Product.objects.all()
                ruyxat = []
                for item in data:
                    serializers = ProductSerializers(item).data
                    ruyxat.append(serializers)
                return Response(ruyxat)
            
        


        