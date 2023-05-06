from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView, TokenVerifyView
from django.views.decorators.cache import cache_page




urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),


    path("api/v0/", include("magazin.api.v0.urls")),

    path("cart/", views.ShowCartView.as_view(), name="cart"),

    path("footer/about/", views.AboutView.as_view(), name="about"),
    path("footer/oferta/", views.OfertaView.as_view(), name="oferta"),
    path("footer/oplata/", views.OplataView.as_view(), name="oplata"),
    path("footer/oplata2/", views.Oplata2View.as_view(), name="oplata2"),
    path("footer/dostavka/", views.DostavkaView.as_view(), name="dostavka"),

    path("<str:category_slug>/", cache_page(60*15)(views.ShowProducts.as_view()), name="items_list"),
    path("<str:slug>/<int:id>/", views.ProductView.as_view(), name="show_item"),


    path("cart/add/<int:product_id>/", views.CartAddView.as_view(), name="add-item"),
    path("cart/remove/<int:product_id>/", views.CartRemoveView.as_view(), name="remove-item"),


]
