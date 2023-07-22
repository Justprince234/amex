from django.urls import path
from . import views

app_name = 'rentals'

urlpatterns = [
    path('rentals/', views.rentals, name='rentals'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('rental/<slug:slug>/', views.rental, name='rental'),
]