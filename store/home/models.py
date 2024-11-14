from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.IntegerField()
    discount = models.IntegerField()
    Availability = models.BooleanField()
    category = models.CharField(max_length=30)
    seller = models.CharField(max_length=30)

    def __str__(self):
        return self.name