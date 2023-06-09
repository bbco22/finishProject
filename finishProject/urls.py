"""finishProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from user import views as user_views
from orders import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("orders/", include("orders.url"), name="orders"),
    path("", include("magazin.urls")),
    path("account/register", user_views.register, name="sign_up"),
    path("account/", include("django.contrib.auth.urls")),
    path("accounts/profile/", views.ShowOrderView.as_view(), name="profile"),
    path("activate/<uid>/<token>/", user_views.activate, name="activate"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
