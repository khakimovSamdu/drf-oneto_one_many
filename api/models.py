from django.db import models

# Create your models here.

class Contact(models.Model):
    phone = models.CharField(max_length=45)
    address = models.CharField(max_length=124)

    def __str__(self) -> str:
        return self.address

class Student(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
class Company(models.Model):
    name = models.CharField(max_length=124)
    logo = models.CharField(max_length=124)
    description = models.CharField(max_length=125)

    def __str__(self) -> str:
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=126)
    color = models.CharField(max_length=125)
    price = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
