from django.urls import path
from . import views

app_name = 'properties'

urlpatterns = [
    path('properties/', views.properties, name='properties'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('property/<slug:slug>/', views.property, name='property')
]