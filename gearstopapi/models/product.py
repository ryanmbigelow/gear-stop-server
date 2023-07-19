from django.db import models
from .user import User
from .category import Category

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    quantity_available = models.IntegerField()
    price = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(User, on_delete=models.CASCADE)
