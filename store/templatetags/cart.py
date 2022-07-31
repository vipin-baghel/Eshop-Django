from django import template

register = template.Library()


@register.filter(name='qty_in_cart')
def qty_in_cart(product, cart):
    quantity = cart.get(str(product.id))
    print(f"checking product {product.id} in cart {cart}, found quantity {quantity}")
    return int(quantity)


@register.filter(name='amt_product')
def amt_product(product, cart):
    return product.price * qty_in_cart(product, cart)


@register.filter(name='total_cart_amt')
def total_cart_amount(products, cart):
    sum = 0
    for p in products:
        sum += amt_product(p, cart)
    return sum