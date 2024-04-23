from rest_framework import serializers
from .models import Student, Contact
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

