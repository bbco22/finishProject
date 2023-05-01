from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics


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

class OrdersListAPIViewGEN(generics.ListAPIView):
    """смотрим и создаём заказы"""

    queryset = Order.objects.all()
    serializer_class = OrdersSerializer


class OrderControlAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrdersSerializer
    lookup_url_kwarg = "order_id"
    lookup_field = "id"





class DetailOrderItemAPIView(APIView):

    def get(self, request, item_id: int):
        order = get_object_or_404(OrderItem, id=item_id)
        serializer = OrderItemSerializer(order)
        return Response(serializer.data)



