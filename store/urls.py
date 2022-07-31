from django.urls import path

from .middlewares.auth import auth_middleware
from .views.cart import Cart
from .views.checkout import Checkout
from .views.login import Login, logout
from .views.orders import Orders
from .views.signup import Signup
from .views.home import Home

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup', Signup.as_view(), name='signuppage'),
    path('login', Login.as_view(), name='loginpage'),
    path('logout', logout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('checkout', Checkout.as_view(), name='checkout'),
    path('orders', auth_middleware(Orders.as_view()), name='orders')

]
