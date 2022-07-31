from django.views import View
from django.shortcuts import render, redirect

from store.models import Order


class Orders(View):
    def post(self, request):
        pass

    def get(self, request):
        cid = request.session.get('cid')
        orders = Order.get_orders_by_cid(cid)
        print(orders)
        return render(request, 'orders.html', {'orders': orders})
