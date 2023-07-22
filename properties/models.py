from django.db import models
from django.urls import reverse

# Create your models here.
Status = (
    ('For Sale', 'For Sale'),
    ('For Rent', 'For Rent')
)

class Property(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    status = models.CharField(choices=Status, default= "For Sale", max_length=10)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=50, decimal_places=2)
    number_of_bedroom = models.IntegerField(null=True, blank=True)
    number_of_bathroom = models.IntegerField(null=True, blank=True)
    living_area = models.CharField(max_length=20,  default='Not Available')
    lot_size = models.CharField(max_length=20, default='Not Available')
    available = models.BooleanField(default=True)


    class Meta:
        verbose_name_plural = "Property Listings"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('properties:property', args=[self.slug])
    
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
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.full_name