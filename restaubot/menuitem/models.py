from django.db import models


class MenuItem(models.Model):

    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='menu_items')
    name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    cuisine = models.CharField(max_length=100, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    inventory_status = models.CharField(max_length=20, default='in_stock')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [ 
            models.UniqueConstraint(fields=['name', 'user'], name='unique_menu_item_per_user')
        ]

    def __str__(self):
        return f"{self.name} ({self.cuisine})"
    
    def update_inventory_status(self, new_status):
        if new_status != self.inventory_status:
            self.inventory_status = new_status
            self.save()

    def update_rating(self, new_rating):
        if new_rating != self.rating:
            self.rating = new_rating
            self.save()