from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# My apps
from .models import User

# Create your views here.
def registration(request):
    """Displays the account application page."""
    template_name = 'signup.html'
    if request.method == 'POST':
        full_name = request.POST['full_name']
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            messages.error(request, 'Password does not match')
            return redirect('core:registration')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'E-mail already exist.')
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already exist.')
                return redirect('core:home')
        user = User.objects.create_user(full_name=full_name, username=username, email=email, phone=phone, password=password)
        user.save()
        return redirect('accounts:login')
    return render(request, template_name)

def login(request):
    """Displays the account login page."""
    template_name = 'login.html'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('core:home')
        messages.info(request, 'Invalid Credentials.')
        return redirect('accounts:login')
    return render(request, template_name)

def logout(request):
    """Returns the logout page, redirecting to the home page."""
    auth.logout(request)
    return redirect('core:home')