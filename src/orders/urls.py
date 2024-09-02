from django.urls import path
from . import views as orders

app_name = "orders"
urlpatterns = [
    path("cart/", orders.view_cart, name="view_cart"),
    path("add_to_cart/", orders.add_to_cart_view, name="add_to_cart"),
    path("evaluate/", orders.evaluate_cart, name="evaluate_cart"),
    path("create_order/", orders.CreateOrderView.as_view(), name="create_order"),
    path("ordered/", orders.Ordered.as_view(), name="ordered"),
]