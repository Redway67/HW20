from django.urls import path
from hotelapp import views


app_name = 'hotelapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('booking/', views.booking, name='booking'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
]