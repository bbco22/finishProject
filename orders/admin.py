from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ["product"]


class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email",
                    "address", "payment",
                    "created", "updated"]
    list_filter = ["payment", "created", "updated"]
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
