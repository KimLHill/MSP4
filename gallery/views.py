from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Gallery
from .forms import GalleryForm

# View for gallery page
def gallery(request):
    """ A view to show gallery page """

    gallery = Gallery.objects.all()
    
    context = {
        'gallery': gallerys,
    }

    return render(request, 'gallery/gallery.html', context)


# View for gallery details
def gallery_detail(request, gallery_id):
    """ A view to show individual gallery page """

    gallery = get_object_or_404(Gallery, pk=gallery_id)

    context = {
        'gallery': gallery,
    }

    return render(request, 'gallery/gallery_detail.html', context)


@login_required
def add_gallery(request):
    # Add a gallery to the site 
    if not request.user.is_superuser:
        # Only superusers can add images
        messages.error(request, 'Sorry, only store owners can add an image.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            # If valid, save form
            gallery = form.save()
            # Show success message
            messages.success(request, 'Successfully added image to gallery!')
            # Take user to that image's details page
            return redirect(reverse('gallery_detail', args=[gallery.id]))
        else:
            # If invalid, show error message
            messages.error(request, 'Failed to add image. Please ensure the form is valid.')
    else:
        form = GalleryForm()
        
    template = 'gallery/add_gallery.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_gallery(request, gallery_id):
    """ Edit an image in the gallery """
    if not request.user.is_superuser:
        # Only superusers can edit products
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    gallery = get_object_or_404(Gallery, pk=gallery_id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated gallery!')
            return redirect(reverse('gallery_detail', args=[gallery.id]))
        else:
            messages.error(request, 'Failed to update gallery. Please ensure the form is valid.')
    else:
        form = GalleryForm(instance=gallery)
        messages.info(request, f'You are editing {gallery.name}')

    template = 'gallery/edit_gallery.html'
    context = {
        'form': form,
        'gallery': gallery,
    }

    return render(request, template, context)


@login_required
def delete_gallery(request, gallery_id):
    if not request.user.is_superuser:
        # Only superusers can delete images
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get image
    gallery = get_object_or_404(Gallery, pk=gallery_id)
    # Delete image
    gallery.delete()
    # Image successfully deleted message
    messages.success(request, 'Image deleted!')
    # Redirect back to gallery page
    return redirect(reverse('gallery'))


