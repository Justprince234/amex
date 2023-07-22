from django.shortcuts import render, get_object_or_404, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib import messages


from .models import Vehicle_Specification, Contact

# Create your views here.
def rentals(request):
    """ A view to show individual product details """
    template = 'rentals.html'
    products = Vehicle_Specification.objects.filter(available=True)
    context = {'products': products}

    return render(request, template, context)


def rental(request, slug):
    """ A view to show individual product details """
    template = 'rental.html'
    product = get_object_or_404(Vehicle_Specification, slug=slug, available=True)

    context = {
        'product': product,
    }

    return render(request, template, context)

def contact_us(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        passport = request.FILES['passport']
        fs = FileSystemStorage()
        file = fs.save(passport.name, passport)
        contact = Contact.objects.create(full_name=name, passport=file, email=email, message=message)
        contact.save()
        messages.success(request, 'Message Sent!')
        return redirect('rentals:rentals')