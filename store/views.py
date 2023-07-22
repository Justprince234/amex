from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm


from .models import Product

# Create your views here.
def products(request):
    """ A view to show individual product details """
    template = 'shop.html'
    products = Product.objects.filter(available=True)
    context = {'products': products}

    return render(request, template, context)


def product(request, slug):
    """ A view to show individual product details """
    template = 'pro-details.html'
    product = get_object_or_404(Product, slug=slug, available=True)
    cart_product_form = CartAddProductForm()

    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }

    return render(request, template, context)