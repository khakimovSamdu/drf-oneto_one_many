from rest_framework import serializers
from .models import Student, Contact, Company, Product
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
