from django.db import models

# Create your models here.
class restaurants(models.Model):
    restaurant_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)
    rating = models.IntegerField()
    reviews = models.CharField(max_length=200)
    image = models.ImageField(upload_to='restaurants/', blank=True, null=True)
    description = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)
    