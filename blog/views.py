from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    """ A view to show individual blog page """

    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_detail.html', context)


# Require user to be logged in to add a blog
@login_required
def add_blog(request):
    # Add a blog to the site 
    if not request.user.is_superuser:
        # Only superusers can add products
        messages.error(request, 'Sorry, only store owners can add a blog.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            # If valid, save form
            blog = form.save()
            # Show success message
            messages.success(request, 'Successfully added blog!')
            # Take user to that blog's details page
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            # If invalid, show error message
            messages.error(request, 'Failed to add blog. \
                Please ensure the form is valid.')
    else:
        form = BlogForm()
        
    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# Require user to be logged in to edit a blog
@login_required
def edit_blog(request, blog_id):
    """ Edit a blog in the store """
    if not request.user.is_superuser:
        # Only superusers can edit products
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            # If valid, save form
            form.save()
            # Show success message
            messages.success(request, 'Successfully updated blog!')
            # Take user to that blog's details page
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update blog. \
                Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.name}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)


# Require user to be logged in to delete a blog
@login_required
def delete_blog(request, blog_id):
    if not request.user.is_superuser:
        # Only superusers can delete blogs
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get blog
    blog = get_object_or_404(Blog, pk=blog_id)
    # Delete blog
    blog.delete()
    # Blog successfully deleted message
    messages.success(request, 'Blog deleted!')
    # Redirect back to products page
    return redirect(reverse('blog'))
