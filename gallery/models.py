from django.db import models

# Blog model. Requires name, author and description. 
class Gallery(models.Model):

    # Change gallerys to galleries
    class Meta:
        verbose_name_plural = 'Galleries'

    name = models.CharField(max_length=254)
    author = models.CharField(max_length=254)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name