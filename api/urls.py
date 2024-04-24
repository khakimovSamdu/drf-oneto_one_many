from django.urls import path
from .views import OneTOGet, OneToOneContact, OnetoMenyCompany, OnetoMenyProduct

urlpatterns = [
    path('get/students', OneTOGet.as_view()),
    path('get/students/id/<int:id>/', OneTOGet.as_view()),
    path('get/students/contact/<int:contact>/', OneTOGet.as_view()),
    path('get/contacts/id/<int:id>/', OneToOneContact.as_view()),
    path('get/contacts/', OneToOneContact.as_view()),
    path('post/contacts/add/', OneToOneContact.as_view()),
    path('get/company/id/<int:id>/', OnetoMenyCompany.as_view()),
    path('get/company/', OnetoMenyCompany.as_view()),
    path('get/product/id/<int:id>', OnetoMenyProduct.as_view()),
    path('get/product/', OnetoMenyProduct.as_view()),


]