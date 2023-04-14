from django.urls import path,include
from . import views

urlpatterns = [
    
    path('',include('authentication.urls')), # Authentication section
    path('', views.index, name='index')
]
