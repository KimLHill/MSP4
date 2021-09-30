from django.contrib import admin
from .models import Blog

# Blog information


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'author',
        'description',
        'image',
    )

    ordering = ('name',)


admin.site.register(Blog, BlogAdmin)
