from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    message = models.TextField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    available = models.BooleanField(default=True)