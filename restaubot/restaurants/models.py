from django.db import models

# Create your models here.
class restaurants(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)
    price = models.FloatField()
    rating = models.IntegerField()
    reviews = models.CharField(max_length=200)
    menu = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    tags = models.CharField(max_length=200)
    categories = models.CharField(max_length=200)