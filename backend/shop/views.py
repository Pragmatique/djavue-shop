from django.shortcuts import render_to_response
from rest_framework import viewsets

from .models import Product, Order, ProductInOrder
from .serializers import ProductSerializer, OrderSerializer, ProductInOrderSerializer


def index(request):
    return render_to_response('index.html')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderSerializer

class ProductInOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductInOrder.objects.all()
    serializer_class = ProductInOrderSerializer
