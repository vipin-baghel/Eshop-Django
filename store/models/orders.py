from django.utils.timezone import now
from django.db import models
from store.models import Product, Customer


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    amount = models.IntegerField(default=0)
    date = models.DateField(default=now())
    address = models.CharField(default="", max_length=100)
    status = models.IntegerField(default=0)

    def place_order(self):
        self.save()

    def get_orders_by_cid(cid):
        return Order.objects.filter(customer=cid).order_by('date')
