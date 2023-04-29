from rest_framework import serializers
from ...models import Product, Category
from orders.models import Order, OrderItem


class ProductsSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class DetailProductSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategoriesSerializer(serializers.ModelSerializer):
    url = serializers.CharField(source="get_absolute_url", read_only=True)

    class Meta:
        model = Category
        fields = "__all__"


class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ["email", "updated"]

class OrderItemSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="order.name", read_only=True)

    class Meta:
        model = OrderItem
        fields = "__all__"

