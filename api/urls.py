from django.urls import path
from .views import OneTOGet

urlpatterns = [
    path('get/', OneTOGet.as_view()),
    
]