from django.db import models
from django.urls import reverse


# Create your models here.
class Vehicle_Specification(models.Model):
    """Creates a database instance Item in database."""
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    price = models.DecimalField(default=0, max_digits=50, decimal_places=2)
    make = models.CharField(max_length=50)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    model = models.CharField(max_length=50)
    year = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    engine_type = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Car rentals"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rentals:rental', args=[self.slug])
    

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
        
    @property
    def image4URL(self):
        if self.photo_4:
            return self.photo_4.url
        else:
            return "/static/img/Placeholder.png"
        
class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    passport = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name