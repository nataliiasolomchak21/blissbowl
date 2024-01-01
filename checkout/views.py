from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from cart.contexts import cart_contents

import stripe

def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    current_cart = cart_contents(request)
    total = current_cart['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OJyBZLDXfeZuIluVChtkPuGC18AfmecBXtdey7YLn34t73syTUDqMb3cvgbn2KGEd9yVgkh77Zk41GLOzg5a1yY007YAya5ge',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)

