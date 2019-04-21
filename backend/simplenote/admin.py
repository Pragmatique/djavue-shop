from django.contrib import admin
from shop.models import Product, Order, ProductInOrder
from accounts.models import UserManager, User

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(ProductInOrder)
admin.site.register(User)
