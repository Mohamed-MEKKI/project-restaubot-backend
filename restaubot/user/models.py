from django.db import models


class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    number_of_orders = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='active')
    password = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def is_authenticated(self):
        return True