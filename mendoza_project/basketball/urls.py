from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('basketball/', views.basketball, name='basketball'),
    path('about', views.about, name='about'),
]