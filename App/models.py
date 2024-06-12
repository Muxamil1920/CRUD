from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(max_length=280)
    file = models.ImageField(upload_to='products/',unique=True,null=True)
    
    def __str__(self):
        return self.name
    
