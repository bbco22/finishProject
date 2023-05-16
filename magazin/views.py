from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Category, Product
from .filters import MediaDocsFiler
from .cart import Cart
from .forms import CartAddProductForm



class MenuView(View):

    def get(self, request):
        categories = Category.objects.all()
        return render(request, "base.html", {"categories": categories})



class HomeView(View):


    def get(self,request):
        categories = Category.objects.all()

        return render(request,
                      "home.html",
                      {"categories": categories}
                      )


class ShowProducts(View):

    def get(self, request, category_slug=None):
        category = None
        categories = Category.objects.all()
        products = Product.objects.filter(available=True)
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)
            print(products)
        return render(request,
                      "items_list.html",
                      {"category": category,
                       "categories": categories,
                       "products": MediaDocsFiler(request.GET, products).qs}
                      )


class ProductView(View):

    def get(self, request, id, slug):
        product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
        cart_product_form = CartAddProductForm()
        return render(request,
                      "show_item.html",
                      {"product": product,
                       "cart_product_form": cart_product_form}
                      )

class CartAddView(View):

    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                     quantity=cd["quantity"],
                     update_quantity=cd["update"])
            return redirect("cart")

class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect("cart")


class ShowCartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, "cart.html", {"cart": cart})


class AboutView(View):
    def get(self, request):
        return render(request, "footer/about.html")

class OfertaView(View):

    def get(self, request):
        return render( request, "footer/oferta.html")

class OplataView(View):
    def get(self,request):
        return render( request, "footer/oplata.html")


class Oplata2View(View):
    def get(self, request):
        return render(request, "footer/oplata2.html")

class DostavkaView(View):
    def get(self, request):
        return render(request, "footer/dostavka.html")

