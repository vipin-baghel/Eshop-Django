from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=1000, default='', null=True, blank=True)
    image = models.ImageField(upload_to='uploads/products_img/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def get_products_by_ids(id_list: list):
        return Product.objects.filter(id__in=id_list)

    def get_all_products():
        return Product.objects.all()

    def get_products_by_categoryid(c_id):
        if c_id:
            return Product.objects.filter(category=c_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name
