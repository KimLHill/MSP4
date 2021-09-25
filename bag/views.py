from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Get quantity from form and convert to integer
    quantity = int(request.POST.get('quantity'))
    # Get redirect URL to return user to the same page
    redirect_url = request.POST.get('redirect_url')
    # Get the bag variable if it exists in the session or create one
    bag = request.session.get('bag', {})

    # Add item to bag or update quantity if already in bag
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Get quantity from form and convert to integer
    quantity = int(request.POST.get('quantity'))
    # Get the bag variable if it exists in the session or create one
    bag = request.session.get('bag', {})

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
