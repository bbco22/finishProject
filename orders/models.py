from django.db import models
from magazin.models import Product


class Order(models.Model):
    PAYMENT_TYPE = (("card", "Картой"), ("money", "Наличными"))
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    payment = models.CharField(choices=PAYMENT_TYPE, max_length=5)
#    STATUS_TYPE = (("created", "Создан"), ("processing", " В обработке"), ("shipped", "В Доставке"), ("delivered", "Доставлен"))
#   status = models.CharField(choices=STATUS_TYPE, max_length=10)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="order_items", on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.cost * self.quantity
