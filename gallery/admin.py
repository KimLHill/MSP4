from django.contrib import admin
from .models import Gallery

# Register your models here.

class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'description',
        'image',
    )

    ordering = ('name',)


admin.site.register(Gallery, GalleryAdmin)

