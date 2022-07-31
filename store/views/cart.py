from django.shortcuts import render, redirect
from store.models import Product
from django.views import View


class Cart(View):
    def post(self, request):
        print("inside cart.py,  POST method")
        pid = request.POST.get('pid')
        rem = request.POST.get('rem')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(pid)
            if rem:
                if quantity == 1:
                    cart.pop(pid)
                else:
                    cart[pid] = quantity - 1
            else:
                if quantity is None:
                    cart[pid] = 1
                else:
                    cart[pid] = quantity + 1
        else:
            cart = {}
            cart[pid] = 1

        request.session['cart'] = cart
        return redirect('cart')

    def get(self, request):
        print("inside cart.py,  GET method")
        print('you are customer id :', request.session.get('cid'))
        print('your cart:', request.session.get('cart'))
        if request.session.get('cart') is not None:
            item_ids = request.session.get('cart').keys()
            if len(item_ids) > 0:
                items = Product.get_products_by_ids(item_ids)
                return render(request, 'cart.html', {'products': items})
            else:
                return render(request, 'cart_empty.html')
        else:
            return render(request, 'cart_empty.html')
