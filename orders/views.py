from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .models import OrderItem, Order
from cart.cart import Cart

# Create your views here.
@login_required
def order_create(request):
    cart = Cart(request)
    user = request.user
    if request.method == 'POST':
        carttotal = cart.get_total_price()
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        address = request.POST['address']
        state = request.POST['state']
        postal_code = request.POST['postal_code']
        country = request.POST['country']
        order = Order.objects.create(user=user, first_name=first_name, last_name=last_name, phone=phone, address=address, state=state,
        postal_code=postal_code, country=country)
        order.amount = cart.get_total_price()
        order.save()
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'],price=item['price'],quantity=item['quantity'])
        # set the order in the session
        request.session['order_id'] = order.id
        # clear the cart
        cart.clear()
        
        return redirect('amex:payment')
    return render(request, 'checkout.html', {'carttotal': carttotal})