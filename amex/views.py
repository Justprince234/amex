from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from decimal import Decimal

from .models import Amex
from orders.models import Order
from transactions.models import History
from travels.models import Flight_Prices, Customer


# Create your views here.
@login_required
def payment(request):
    template_name = 'payment.html'
    user =request.user
    # order_id = request.session.get('order_id')
    order = Order.objects.filter(user=user)[0]
    # order = get_object_or_404(Order, id=order_id)
    total_cost = order.amount
    context = {'orders':order}
    update_amex = Amex.objects.filter(user=user)
    amex_balance = Amex.objects.get(user=user).amount_on_card
    card_num = Amex.objects.get(user=user).card_number
    ccv1 = Amex.objects.get(user=user).ccv
    pin1 = Amex.objects.get(user=user).pin
    date = Amex.objects.get(user=user).expiry_date
    if request.method == 'POST':
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        ccv = request.POST['ccv']
        pin = request.POST['pin']
        
        if card_num==card_number and ccv1==int(ccv) and pin1==int(pin) and date==expiry_date:
            if Decimal(total_cost) > amex_balance:
                messages.info(request, "Insufficient Balance")
                return redirect('core:payment')
            amex_balance -= total_cost
            update_amex.update(amount_on_card=amex_balance)
            order.paid = True
            order.save()
            histories = History.objects.create(user=user, amount=total_cost)
            histories.save()
            return redirect('amex:success')
        messages.info(request, "Invalid Card Information")
        return redirect('amex:payment')
    return render(request, template_name, context)

@login_required
def flight_payment(request):
    template_name = 'flight-payment.html'
    user =request.user
    flight_prices = Flight_Prices()
    economy_price = flight_prices.economy_class
    business_price = flight_prices.business_class
    private_price = flight_prices.private_flight
    customers = Customer.objects.filter(user=user)[0]
    flight = customers.flight_class
    print(flight)
    context = {'customers': customers}
    update_amex = Amex.objects.filter(user=user)
    amex_balance = Amex.objects.get(user=user).amount_on_card
    card_num = Amex.objects.get(user=user).card_number
    ccv1 = Amex.objects.get(user=user).ccv
    pin1 = Amex.objects.get(user=user).pin
    date = Amex.objects.get(user=user).expiry_date
    if request.method == 'POST':
        card_number = request.POST['card_number']
        expiry_date = request.POST['expiry_date']
        ccv = request.POST['ccv']
        pin = request.POST['pin']

        if card_num==card_number and ccv1==int(ccv) and pin1==int(pin) and date==expiry_date:
            if flight == "Economy":
                if economy_price > amex_balance:
                    messages.info(request, "Insufficient Balance")
                    return redirect('amex:flight_payment')
            
                amex_balance -= economy_price
                update_amex.update(amount_on_card=amex_balance)
                customers.paid =True
                customers.save()
                return redirect('travels:customer-data')
                  
            if flight == "Business":
                if business_price > amex_balance:
                    messages.info(request, "Insufficient Balance")
                    return redirect('amex:flight_payment')
                
                amex_balance -= business_price
                update_amex.update(amount_on_card=amex_balance)
                customers.paid =True
                customers.save()
                return redirect('travels:customer-data')
            
            if flight == "Private":
                if private_price > amex_balance:
                    messages.info(request, "Insufficient Balance")
                    return redirect('amex:flight_payment')

                amex_balance -= private_price
                update_amex.update(amount_on_card=amex_balance)
                customers.paid =True
                customers.save()
                return redirect('travels:customer-data')
        messages.info(request, "Invalid Card Information")
        return redirect('amex:flight_payment')
    return render(request, template_name, context)

def success(request):
    user =request.user
    # order_id = request.session.get('order_id')
    order = Order.objects.filter(user=user)[0]
    # order = get_object_or_404(Order, id=order_id)
    context = {'orders':order}
    template_name = 'success.html'
    return render(request, template_name, context)

def failure(request):
    template_name = 'failure.html'
    return render(request, template_name)