from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    # set total and product count to 0 to start count from
    total = 0
    product_count = 0
    # Get bag from session if one or create one
    bag = request.session.get('bag', {})

    # Add up total cost and product count of shopping bag contents
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })
    # Add delivery charge if total less than threshold
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = 0
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        # Free delivery if total more than threshold
        delivery = 0
        free_delivery_delta = 0
    # Calculate bag total
    grand_total = delivery + total
    
    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
