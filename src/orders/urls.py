from django.urls import path, include

from . import apiviews
from . import views as orders

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'api-book-in-cart', apiviews.BookInCartViewSet)

app_name = "orders"
urlpatterns = [
    path("cart/", orders.view_cart, name="view_cart"),
    path("add_to_cart/", orders.add_to_cart_view, name="add_to_cart"),
    path("evaluate/", orders.evaluate_cart, name="evaluate_cart"),
    path("create_order/", orders.CreateOrderView.as_view(), name="create_order"),
    path("ordered/", orders.SuccesufulOrder.as_view(), name="ordered"),
    path("ordered_orders/", orders.Orders.as_view(), name="ordered_orders"),
    path("order_detail/<int:pk>", orders.OrderDetail.as_view(), name="order_detail"),
]

urlpatterns = urlpatterns + router.urls