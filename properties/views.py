from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Property, Contact, Apartment

def properties(request):
    """Displays the properties page."""
    properties  = Property.objects.filter(available=True)
    apartments  = Apartment.objects.filter(available=True)
    template_name = 'properties.html'
    context = {'properties': properties, 'apartments':apartments}
    return render(request, template_name, context)

def apartment(request, slug):
    """Displays the blog page."""
    apartment = get_object_or_404(Apartment, slug=slug, available=True)
    template_name = 'apartment.html'
    return render(request, template_name, {'apartment': apartment})

def property(request, slug):
    """Displays the blog page."""
    property = get_object_or_404(Property, slug=slug, available=True)
    template_name = 'pro.html'
    return render(request, template_name, {'properties': property})

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        contact = Contact.objects.create(full_name=name, email=email, message=message)
        contact.save()
        messages.success(request, 'Message Sent!')
        return redirect('properties:properties')