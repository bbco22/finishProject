from django.urls import path, include
from django.views.generic import TemplateView
from . import views

# /api/v0


urlpatterns = [

    path("products/", views.ListProductAPIView.as_view()),
    path("product/<int:product_id>/", views.DetailProductAPIView.as_view()),
    path("categories/", views.ListCategoryAPIView.as_view()),
    path("orders/", views.OrdersListAPIViewGEN.as_view()),
    path("order/<int:order_id>/", views.OrderControlAPIView.as_view()),

]
