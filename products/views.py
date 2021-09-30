from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


# Code created from following Code Institute Boutique Ado tutorial videos
# View for all products
def all_products(request):
    """ A view to show individual product details """

    products = Product.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            # Get requested data
            query = request.GET['q']
            if not query:
                # Error message if performed with no search criteria entered
                messages.error(request, "Please enter your search criteria!")
                # Redirect back to products
                return redirect(reverse('products'))
            
            # Return results when search criteria matches name or description
            queries = Q(name__icontains=query) | Q(
                        description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
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


# Login required to add product
@login_required
def add_product(request):
    # Add a product to the store 
    if not request.user.is_superuser:
        # Only superusers can add products
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # If valid, save form
            product = form.save()
            # Show success message
            messages.success(request, 'Successfully added product!')
            # Take user to that product's details page
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # If invalid, show error message
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Login required to edit product
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        # Only superusers can edit products
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Login required to delete product
@login_required
def delete_product(request, product_id):
    if not request.user.is_superuser:
        # Only superusers can delete products
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get product
    product = get_object_or_404(Product, pk=product_id)
    # Delete product
    product.delete()
    # Product successfully deleted message
    messages.success(request, 'Product deleted!')
    # Redirect back to products page
    return redirect(reverse('products'))

