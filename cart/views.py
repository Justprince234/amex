from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from store.models import Product
from django.contrib import messages
from django.http import JsonResponse
from .cart import Cart
from .forms import CartAddProductForm

   
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'], override_quantity=cd['override'])
        messages.success(request, 'Successfully added product!')
        quantity = cart.__len__()
        response = JsonResponse({'quantity': quantity})
    return redirect('store:products')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    messages.success(request, 'Item deleted!')
    return redirect('cart:checkout')

def checkout(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
    return render(request, 'checkout.html', {'cart': cart})