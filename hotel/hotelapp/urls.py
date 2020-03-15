from django.urls import path
from hotelapp import views


app_name = 'hotelapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('booking/', views.BookingCreateView.as_view(), name='booking'),
    path('gallery/', views.GalleryView.as_view(), name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('administration/', views.AdmListView.as_view(), name='administration'),
]