from django.contrib import admin
from .models import Student, Contact, Company, Product
# Register your models here.

admin.site.register(Student)
admin.site.register(Contact)
admin.site.register(Company)
admin.site.register(Product)

