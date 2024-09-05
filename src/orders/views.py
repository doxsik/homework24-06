from django.forms import BaseModelForm
from django.shortcuts import render
from django.views import generic
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from books.models import Book
from . import models, forms

# Create your views here.

def get_customer_adress(request):
    adress = request.user.profile
    adress = f"Index: {adress.index}; Country: {adress.country}; City: {adress.city}; Street: {adress.street_house}"
    return adress

def get_customer_phone(request):
    phone = request.user.profile.phone
    return phone

def get_or_create_cart(request):
    cart_id = request.session.get("cart_id", None)
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user
    cart, created = models.Cart.objects.get_or_create(pk=cart_id, defaults={"user":user})
    if created:
        request.session["cart_id"] = cart.pk
    return cart

def get_current_cart(request):
    cart_id = request.session.get("cart_id", None)
    cart = models.Cart.objects.filter(pk=cart_id)
    if cart:
        cart = cart[0]
    else:
        cart = bool(cart)
    return cart

def fake_delete_cart(request):
    cart = get_current_cart(request)
    has_book = models.BookInCart.objects.filter(cart=cart)
    if not has_book:
        request.session['cart_id'] = None

def view_cart(request):
    cart = get_current_cart(request)
    context = {"cart": cart}
    return render(request, template_name="orders/view_cart.html", context=context)

def add_to_cart(request):
    book_id = request.POST.get("book_id")
    quantity = int(request.POST.get("quantity"))
    cart = get_or_create_cart(request)
    book = Book.objects.get(pk=book_id)
    book_in_cart, created = models.BookInCart.objects.get_or_create(
        cart=cart, 
        book=book,
        defaults={"quantity":quantity, "price":book.price},
    )
    if not created:
        book_in_cart.quantity += quantity
        book_in_cart.save()

def add_to_cart_view(request):
    if request.method == "POST":
        add_to_cart(request)
    return HttpResponseRedirect(reverse_lazy("orders:view_cart"))

def create_order(request):
    cart = get_or_create_cart(request)
    
def update_cart(key, quantity):
    book_in_cart_id = int(key.split(".")[1])
    book_in_cart = models.BookInCart.objects.get(pk=book_in_cart_id)
    no_books = models.BookInCart.objects.all()
    if int(quantity) == 0:
        book_in_cart.delete()
    else:
        book_in_cart.quantity = int(quantity)
        book_in_cart.save()
    
def evaluate_cart(request):
    if request.method == "POST":
        action = None
        for key, value in request.POST.items():
            if key[0:4] == "quan":
                update_cart(key, value)
            if key[0:4] == "acti":
                action = value
        if action == "update":
            fake_delete_cart(request)
            return HttpResponseRedirect(reverse_lazy("orders:view_cart"))
        elif action == "create":
            return HttpResponseRedirect(reverse_lazy("orders:create_order"))


class CreateOrderView(generic.CreateView):
    model = models.Order
    form_class = forms.CreateOrderForm
    template_name = "orders/create_order.html"
    success_url = reverse_lazy("orders:ordered")

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        form.fields["phone"].initial = get_customer_phone(self.request)
        form.fields["adress"].initial = get_customer_adress(self.request)
        return form
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = get_current_cart(self.request)
        return context
    
    def form_valid(self, form):
        order = form.save(commit=False)
        order.cart = get_current_cart(self.request)
        order.save()
        self.object = order
        return HttpResponseRedirect(self.get_success_url())
    
class Ordered(generic.TemplateView):
    template_name = "orders/ordered.html"
    
    def get(self, request, *args, **kwargs):
        request.session['cart_id'] = None
        return super().get(request, *args, **kwargs)