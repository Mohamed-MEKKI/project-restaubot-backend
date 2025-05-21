from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    cuisine = models.CharField(max_length=100, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    inventory_status = models.CharField(max_length=20, default='in_stock')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name
    
    def update_inventory_status(self, new_status):
        if new_status != self.inventory_status:
            self.inventory_status = new_status
            self.save()

    def update_rating(self, new_rating):
        if new_rating != self.rating:
            self.rating = new_rating
            self.save()
