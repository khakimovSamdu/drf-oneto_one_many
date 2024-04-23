from django.urls import path
from .views import OneTOGet, OneToOneContact

urlpatterns = [
    path('get/students', OneTOGet.as_view()),
    path('get/students/id/<int:id>/', OneTOGet.as_view()),
    path('get/students/contact/<int:contact>/', OneTOGet.as_view()),
    path('get/contacts/id/<int:id>/', OneToOneContact.as_view()),
    path('get/contacts/', OneToOneContact.as_view()),
    path('post/contacts/add/', OneToOneContact.as_view()),
    

]