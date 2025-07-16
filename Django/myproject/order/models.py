from django.db import models


# Create your models here.

class product(models.Model):
    STATUS = [
        {'P': 'Pending'},
        {'C': 'Completed'},
        {'F': 'Failed'}
    ]
    
    class products(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        model = models.DecimalField(max_length=100)        
        description = models.TextField(null=True, blank=True)
        stock = models.PositiveIntegerField(default=0)  
        slug = models.SlugField(unique=True)