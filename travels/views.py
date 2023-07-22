from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from .models import Bookings, Customer

# Create your views here.
def bookings(request):
    """Displays the index page."""
    template_name = 'booking.html'
    if request.method == 'POST':
        home = request.POST.get('home')
        destination = request.POST.get('destination')

        bookings = Bookings.objects.create(home=home, destination=destination)
        bookings.save()
        return redirect('travels:booking-upload')
    return render(request, template_name)


@login_required
def booking_slip(request):
    user = request.user
    template_name = 'booking-validation.html'
    if request.method == 'POST' and request.FILES['passport']:
        flight_class = request.POST.get('flight_class')
        name = request.POST['name']
        passport = request.FILES['passport']
        fs = FileSystemStorage()
        file = fs.save(passport.name, passport)
        customer = Customer.objects.create(user=user, flight_class=flight_class, name=name, passport=file)
        customer.save()
        return redirect('amex:flight_payment')
    return render(request, template_name)

def customer_data(request):
    template_name = 'slip.html'

    return render(request, template_name)