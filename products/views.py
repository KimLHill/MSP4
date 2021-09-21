from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Code created from following Code Institute Boutique Ado tutorial videos
# View for all products
def all_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            # Get requested data
            query = request.GET['q']
            if not query:
                # Error message if search performed with no search criteria entered
                messages.error(request, "Please enter your search criteria!")
                # Redirect back to products
                return redirect(reverse('products'))
            
            # Return results when search criteria matches in either name or description
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)


# View for product details
def product_detail(request, product_id):
    """ A view to show all products plus sorting and search queries """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)