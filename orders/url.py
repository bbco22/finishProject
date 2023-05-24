from django.urls import path
from . import views


urlpatterns = [
    path("create/", views.order_create, name="order-create"),
    path("check/", views.check_order, name="order-check"),
]
