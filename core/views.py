from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import User
from amex.models import Amex
from blog.models import Blog

# Create your views here.
def home(request):
    """Displays the index page."""
    template_name = 'index.html'
    blogs = Blog.objects.filter(available=True)
    context = {"blogs": blogs}
    return render(request, template_name, context)

@login_required
def dashboard(request):
    """Displays the index page."""
    user = request.user
    template_name = 'dash.html'
    users = User.objects.all()
    amexs = Amex.objects.all
    context = {'users': users, 'amexs':amexs}
    
    return render(request, template_name, context)
