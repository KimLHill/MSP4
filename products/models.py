from django.db import models


# Category model
class Category(models.Model):

    class Meta:
        # Correct spelling of categories
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=150)
    # Optional friendly name
    friendly_name = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# Product model
class Product(models.Model):
    # requires each product to have a name, description and price
    category = models.ForeignKey('Category', null=True, blank=True, 
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, 
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
