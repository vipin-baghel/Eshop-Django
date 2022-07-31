from django.shortcuts import redirect
from django.views import View
from store.models import Product, Order, Customer
from store.templatetags.cart import qty_in_cart, amt_product


class Checkout(View):
    def post(self, request):
        print("inside Checkout, POST method")
        print("address=", request.POST.get('address'), "cid=", request.session.get('cid'))
        address = str(request.POST.get('address')).strip()
        cid = request.session.get('cid')
        cart = request.session.get('cart')
        items = Product.get_products_by_ids(list(cart.keys()))
        for i in items:
            order = Order(customer=Customer.by_cid(cid),
                          product=i,
                          amount=amt_product(i, cart),
                          address=address,
                          quantity=qty_in_cart(i, cart),
                          )
            print(order)
            order.place_order()
        request.session['cart'] = {}
        return redirect('cart')

    def get(self, request):
        print("inside Checkout, GET method")
        print(request.POST)
        return redirect('cart')
