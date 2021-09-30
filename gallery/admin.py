from django.contrib import admin
from .models import Gallery

# Gallery model


class GalleryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'description',
        'image',
    )

    ordering = ('name',)


admin.site.register(Gallery, GalleryAdmin)
