from django.db import models
from .user import User

class Order(models.Model):

    is_open = models.BooleanField(max_length=50)
    is_shipped = models.BooleanField(max_length=50)
    order_total = models.IntegerField()
    payment_method = models.CharField(max_length=100)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
