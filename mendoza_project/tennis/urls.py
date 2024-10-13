from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('tennis/', views.tennis, name='tennis'),
    path('about/', views.about, name='about'),
]