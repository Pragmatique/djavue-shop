from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(max_length=10000, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='products', blank=True, null=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name


######################################################################################


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Opened at')
    closed_at = models.DateTimeField(verbose_name='Closed at', blank=True, null=True)
    is_closed = models.BooleanField(default=False, verbose_name='Is closed')
    is_processed = models.BooleanField(default=False, verbose_name='Is processed')
    phone = models.CharField(max_length=32, null=True)
    address = models.CharField(max_length=256, null=True)
    name = models.CharField(max_length=64, verbose_name='Contact name', null=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def price(self):
        total_price = 0
        for p in self.positions.all():
            total_price += p.price()
        return total_price

######################################################################################

class ProductInOrder(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.ForeignKey('Product',on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Product in Order'
        verbose_name_plural = 'Products in Order'
        ordering = ['-count']

    def price(self):
        return self.product.price * self.count

######################################################################################


