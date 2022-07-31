from django.contrib import admin
from .models import Customer
from .models import Product
from .models import Category
from .models import Order


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name']


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'email']
    search_fields = ['first_name', 'last_name', 'phone', 'email']


class AdminOrder(admin.ModelAdmin):
    list_display = ['product', 'customer', 'amount', 'quantity', 'date', 'address', 'status']
    raw_id_fields = ['customer', 'product']
    search_fields = ['customer__first_name', 'product__name', 'amount', 'quantity', 'date']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer, AdminCustomer)
admin.site.register(Order, AdminOrder)
