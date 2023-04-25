from django.urls import path
from . import views

urlpatterns = [
    path('', views.listing, name='listing'),
    path('offers.html', views.offers, name='offers'),
    path('about.html', views.about, name='about'),
    path('feedback.html', views.feedback, name='feedback'),
    path('map.html', views.map_request, name='map'),
    path('menu.html', views.menu, name='menu'),
    path('more.html', views.more, name='more'),
    path('search.html', views.search, name='search'),
]
