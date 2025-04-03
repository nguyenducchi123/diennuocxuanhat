from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gioi-thieu/', views.about, name='gioi-thieu'),  # Thay about -> gioi-thieu
    path('lien-he/', views.contact, name='lien-he'),      # Thay contact -> lien-he
    path('dich-vu/', views.services, name='dich-vu'),     # Thay services -> dich-vu
    path('san-pham/', views.products, name='san-pham'),   # Thay products -> san-pham
]