from django.db import models
from menuitem.models import MenuItem
from decimal import Decimal



class Order(models.Model):

    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, to_field="name", null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    description = models.TextField(blank=True, editable=False)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    def __str__(self):
        return f"Order: {self.menu_item.name} x{self.name} @ {self.total} "

    def save(self, *args, **kwargs):
        if self.menu_item:
            self.total = self.menu_item.price
            self.description = self.menu_item.description
        else:
            self.total = 0
            self.description = ""
        super().save(*args, **kwargs)

    def update_status(self, new_status, updated_at=None):
        if new_status != self.status:
            self.status = new_status
            self.save()