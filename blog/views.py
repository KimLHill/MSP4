from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Blog
from .forms import BlogForm

# View for blog page
def blog(request):
    """ A view to show blog page """

    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


# View for blog details
def blog_detail(request, blog_id):
    """ A view to show aindividual blog page """

    product = get_object_or_404(Product, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_blog(request):
    # Add a blog to the site 
    if not request.user.is_superuser:
        # Only superusers can add products
        messages.error(request, 'Sorry, only store owners add a blog.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            # If valid, save form
            product = form.save()
            # Show success message
            messages.success(request, 'Successfully added blog!')
            # Take user to that blog's details page
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            # If invalid, show error message
            messages.error(request, 'Failed to add blog. Please ensure the form is valid.')
    else:
        form = ProductForm()
        
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, product_id):
    """ Edit a blog in the store """
    if not request.user.is_superuser:
        # Only superusers can edit products
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog!')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.name}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


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

