from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    path("cart/", views.ShowCartView.as_view(), name="cart"),


    path("<str:category_slug>/", views.ShowProducts.as_view(), name="items_list"),
    path("<str:slug>/<int:id>/", views.ProductView.as_view(), name="show_item"),


    path("cart/add/<int:product_id>/", views.CartAddView.as_view(), name="add-item"),
    path("cart/remove/<int:product_id>/", views.CartRemoveView.as_view(), name="remove-item"),


]