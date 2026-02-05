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
    

class ContactMessages(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    restaurant = models.ForeignKey(restaurants, on_delete=models.CASCADE, related_name='contact_messages')

    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    def send_email(self):
        from django.core.mail import send_mail
        if all(self.message and self.email and self.subject):
            # Assuming you have configured your email settings in Django settings.py
            send_mail(
                subject=self.subject,
                message=self.message,
                from_email="hamidhamidou424@gmail.com",
                to_email=self.email,
            )