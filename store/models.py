from django.db import models
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    """Creates a database instance Item in database."""
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    size = models.CharField( max_length=5)
    color = models.CharField(max_length=50, default="Blue")
    description = models.TextField()
    price = models.DecimalField(default=0, max_digits=50, decimal_places=2)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store:product', args=[self.slug])
    
    @property
    def image1URL(self):
        if self.photo_1:
            return self.photo_1.url
        else:
            return "/static/img/Placeholder.png"
    
    @property
    def image2URL(self):
        if self.photo_2:
            return self.photo_2.url
        else:
            return "/static/img/Placeholder.png"
    
    @property
    def image3URL(self):
        if self.photo_3:
            return self.photo_3.url
        else:
            return "/static/img/Placeholder.png"