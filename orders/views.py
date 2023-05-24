from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from magazin.cart import Cart
from django.views import View


def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item["product"],
                    cost=item["cost"],
                    quantity=item["quantity"],
                )
            # очистка корзины
            cart.clear()
            return render(request, "thanks.html", {"order": order})
    else:
        form = OrderCreateForm
    return render(request, "orders.html", {"cart": cart, "form": form})


def check_order(request):
    order = Order.objects.all()
    if request.method == "POST":
        order.id = request.POST.get("id")
        order = Order.objects.get(id=order.id)
    return render(request, "checkorder.html", {"order": order})


class ShowOrderView(View):
    def get(self, request):
        order = OrderItem.objects.all()
        all_orders = Order.objects.filter(name=request.user)
        print(all_orders)
        for order in all_orders:
           order = OrderItem.objects.filter(order_id=order)
           print(order)

        return render(
            request,
            "profile.html",
            {"orders": all_orders, "product": order},
        )
