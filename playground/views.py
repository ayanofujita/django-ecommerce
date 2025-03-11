from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItem
from django.core.exceptions import ObjectDoesNotExist

def say_hello(request):
    # try:
    #     query_set = Product.objects.all()
    # except ObjectDoesNotExist:
    #     pass
    # print(query_set)
    # for product in query_set:
    #     print(product.title)

    # • Customers with .com accounts
    # • Collections that don’t have a featured product
    # • Products with low inventory (less than 10)
    # • Orders placed by customer with id = 1
    # • Order items for products in collection 3

    data = {
        'customers': Customer.objects.filter(email__endswith=".com"),
        'collections': Collection.objects.filter(featured_product__isnull=True),
        'products': Product.objects.filter(inventory__lt=10),
        'orders': Order.objects.filter(customer_id=1),
        'order_items': OrderItem.objects.filter(product__collection_id=3)
    }

    # for customer in data['customers']: print(customer.first_name, customer.email)
    # for collection in data['collections']: print(collection.title, collection.featured_product)
    # for product in data['products']: print(product.title, product.inventory)
    # for order in data['orders']: print(order.payment_status, order.customer_id)
    # for order_item in data['order_items']: print(Product.objects.get(pk=order_item.product_id).collection_id)
    return render(request, 'hello.html', data)
