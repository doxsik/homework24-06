from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from books.models import Book
from . import models

# Create your views here.
def get_or_create_cart(request):
    cart_id = request.session.get("cart_id", None)
    if request.user.is_anonymous:
        user = None
    else:
        user = request.user
    cart, created = models.Cart.objects.get_or_create(pk=cart_id, defaults={"user":user})
    if created:
        request.session["cart_id"] = cart.pk
        print(cart_id)
    return cart

def get_current_cart(request):
    cart_id = request.session.get("cart_id", None)
    cart = models.Cart.objects.filter(pk=cart_id)
    if cart:
        cart = cart[0]
    else:
        cart = bool(cart)
    return cart

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

def create_order():
    pass

def update_cart(key, quantity):
    book_in_cart_id = int(key.split(".")[1])
    book_in_cart = models.BookInCart.objects.get(pk=book_in_cart_id)
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
            return HttpResponseRedirect(reverse_lazy("orders:view_cart"))
        # create_order()
        # return HttpResponseRedirect(reverse_lazy("orders:view_cart_created"))