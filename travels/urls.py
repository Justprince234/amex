from django.urls import path
from . import views

app_name = 'travels'

urlpatterns = [
    path('bookings', views.bookings, name='bookings'),
    path('booking-upload', views.booking_slip, name='booking-upload'),
    path('customer-data', views.customer_data, name='customer-data'),

]