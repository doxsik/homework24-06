from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse_lazy


# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="cart", blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    @property
    def order_price(self):
        books = self.books.all()
        total_order_price = 0
        for book in books:
            total_order_price += book.total_price
        return total_order_price

    def __str__(self):
        return f"Cart #{self.pk} for {self.user}"
    
class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT, related_name="books")
    book = models.ForeignKey("books.Book", on_delete=models.PROTECT, related_name="book_in_cart")
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(decimal_places=2, max_digits=10)

    @property
    def total_price(self):
        return self.price*self.quantity
    
    def __str__(self):
        return f"Cart #{self.cart.pk} for {self.cart.user} with {self.quantity}"
    
class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.PROTECT, related_name="order")
    phone = models.CharField(verbose_name="Phone", max_length=16)
    adress = models.CharField(max_length=100, verbose_name="Adress")
    
    def get_absolute_url(self):
        return reverse_lazy("orders:order_detail", kwargs = {"pk":self.pk})
    
    def __str__(self):
        return f"Order {self.pk}"