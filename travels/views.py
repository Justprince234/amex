from django.shortcuts import render

# Create your views here.
def booking(request):
    """Displays the index page."""
    template_name = 'booking.html'
    return render(request, template_name)