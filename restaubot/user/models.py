from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    clerk_user_id = models.CharField(max_length=255, unique=True, null=True, blank=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255, blank=True, default='')
    address = models.CharField(max_length=255, blank=True, default='')
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, default='')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @property
    def is_authenticated(self):
        return True