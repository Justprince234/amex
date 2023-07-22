from django.urls import path
from . import views

app_name = 'amex'

urlpatterns = [
    path('payment', views.payment, name='payment'),
    path('flight-payment', views.flight_payment, name='flight_payment'),
    path('success', views.success, name='success'),
    path('failure', views.failure, name='failure')
]