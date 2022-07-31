from django.shortcuts import render, redirect
from store.models import Product
from store.models import Category
from django.views import View


class Home(View):
    def post(self, request):
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
        return redirect('homepage')

    def get(self, request):
        print('you are customer id:', request.session.get('cid'))
        print('your cart:', request.session.get('cart'))
        categories = Category.get_all_categories()
        c_id = request.GET.get('category')
        products = Product.get_products_by_categoryid(c_id)
        return render(request, 'index.html', {'products': products, 'categories': categories})
