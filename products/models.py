from django.db import models
from datetime import timedelta, date
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_new_stock = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        #Automatically unset new stock status after 30 days
        if self.is_new_stock and (self.created_at and (date.today() - self.created_at.date()) > timedelta(days=30)):
            self.is_new_stock = False

        if not self.slug:
            self.slug = models.slugify(self.name) #Generate slug from the name

        super(Product, self).save(*args, **kwargs)

    def  __str__(self) -> str:
        return self.name
    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True, null=True)

    def  __str__(self) -> str:
        return f"Image for {self.product.name}"
    
class OwnerContact(models.Model):
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    whatsapp = models.CharField(max_length=15)

    def  __str__(self) -> str:
        return self.email
    

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def  __str__(self) -> str:
        return self.email