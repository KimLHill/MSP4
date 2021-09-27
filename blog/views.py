from django.shortcuts import render
from .models import Blog

# View for blog page
def blog(request):
    """ A view to show blog page """

    blogs = Blog.objects.all()
    
    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)

