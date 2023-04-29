from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Category, Product
from .filters import MediaDocsFiler
from .cart import Cart
from .forms import CartAddProductForm
from django.views.decorators.http import require_POST



class HomeView(View):

    def get(self,request):
        categories1 = Category.objects.get(id=1)
        categories2 = Category.objects.get(id=2)
        categories3 = Category.objects.get(id=3)

        return render(request,
                      "home.html",
                      {"categories1": categories1,
                       "categories2": categories2,
                       "categories3": categories3}
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
                      {"items": MediaDocsFiler(request.GET, self.products).qs,
                       "category": category,
                       "categories": categories,
                       "products": products}
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


