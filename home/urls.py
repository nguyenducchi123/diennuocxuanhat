from django.urls import path, include  # Import cả path và include
from . import views  # Import views.py

urlpatterns = [
    path('', views.home, name='home'),  
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),  
    path('services/', views.services, name='services'),
    path('products/', views.products, name='products'),  
]
