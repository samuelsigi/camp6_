from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=200)
    address = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Order{self.id} for{self.customer.name}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.item_name} ({self.quantity})'
