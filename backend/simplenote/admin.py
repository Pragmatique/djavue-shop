from django.contrib import admin
from shop.models import Product, Order, ProductInOrder

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductInOrder)