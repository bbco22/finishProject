from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProductsSerializer, DetailProductSerializer, CategoriesSerializer, \
    OrdersSerializer, OrderItemSerializer
from ...models import Product, Category
from orders.models import Order, OrderItem


class ListProductAPIView(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)


class DetailProductAPIView(APIView):

    def get(self, request, product_id: int):
        product = get_object_or_404(Product, id=product_id)
        serializer = DetailProductSerializer(product)
        return Response(serializer.data)



class ListCategoryAPIView(APIView):

    def get(self,request):
        categories = Category.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

class ListOrdersAPIView(APIView):

    def get(self, request):
        orders = Order.objects.all()
        serializer = OrdersSerializer( orders, many=True)
        return Response(serializer.data)



class DetailOrderItemAPIView(APIView):

    def get(self, request, item_id: int):
        order = get_object_or_404(OrderItem, id=item_id)
        serializer = OrderItemSerializer(order)
        return Response(serializer.data)



