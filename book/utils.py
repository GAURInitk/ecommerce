import json
from .models import *


# noinspection PyBroadException
def cookieCart(request):
    try:
        cart_cookie = json.loads(request.COOKIES['cart'])
    except:
        cart_cookie = {}

    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    cartItems = order['get_cart_items']

    for i in cart_cookie:
        try:
            cartItems += cart_cookie[i]['quantity']
            product = Product.objects.get(id=i)
            total = (product.price * cart_cookie[i]['quantity'])
            order['get_cart_total'] += total
            order['get_cart_items'] += cart_cookie[i]['quantity']

            item = {
                'product': {
                    'id': product.id,
                    'name': product.name,
                    'price': product.price,
                    'imageURL': product.imageURL,
                },
                'quantity': cart_cookie[i]['quantity'],
                'get_total': total
            }
            items.append(item)

            if not product.digital:
                order['shipping'] = True
        except:
            pass
    return {'cartItems': cartItems, 'order': order, 'items': items}


def cartData(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    return {'cartItems': cartItems, 'order': order, 'items': items}


def guestOrder(request, data):
    name = data['userData']['name']
    email = data['userData']['email']

    cookieData = cookieCart(request)
    items = cookieData['items']
    customer, created = Customer.objects.get_or_create(
        email=email,
    )
    customer.name = name
    customer.save()

    order = Order.objects.create(
        customer=customer,
        complete=False
    )
    for item in items:
        product = Product.objects.get(id=item['product']['id'])
        OrderItem.objects.create(
            product=product,
            order=order,
            quantity=item['quantity']
        )
    return customer, order
