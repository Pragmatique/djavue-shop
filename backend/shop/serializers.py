from rest_framework import serializers

from .models import Product, Order, ProductInOrder


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id','name', 'description', 'price')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id','created_at', 'closed_at', 'is_closed', 'is_processed', 'phone', 'address', 'name')

    def get_price(self):
        return self.Order.price()



class ProductInOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductInOrder
        fields = ('id','order', 'product', 'count')

    def get_price(self):
        return self.ProductInOrder.price()


