from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    # Get bag from session
    bag = request.session.get('bag', {})
    if not bag:
        # If empty, display error message & return to products page
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JdjpeGCKuMmEVHDHYDMD7kixVSmSja1JFHlRTXum8uk3D4UWqSw7fYEB1Ejivz8ricUz8VvA7tqk0pP7jbWRezg00sUHRBisL',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
