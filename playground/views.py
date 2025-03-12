from django.shortcuts import render
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.db.models import F, Q, Count, Max, Min, Avg, Sum
from store.models import Product, Customer, Collection, Order, OrderItem, Cart, CartItem

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

    # data = {
    #     'customers': Customer.objects.filter(email__endswith=".com"),
    #     'collections': Collection.objects.filter(featured_product__isnull=True),
    #     'products': Product.objects.filter(inventory__lt=10),
    #     'orders': Order.objects.filter(customer_id=1),
    #     'order_items': OrderItem.objects.filter(product__collection_id=3)
    # }

    # for customer in data['customers']: print(customer.first_name, customer.email)
    # for collection in data['collections']: print(collection.title, collection.featured_product)
    # for product in data['products']: print(product.title, product.inventory)
    # for order in data['orders']: print(order.payment_status, order.customer_id)
    # for order_item in data['order_items']: print(Product.objects.get(pk=order_item.product_id).collection_id)

    # find products that have been ordered and sort by title

    # data = Product.objects.filter(orderitem__isnull=False).order_by('title')
    # data = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct()).order_by('title')
    # for product in data: print(product.title, product.orderitem_set.count())

    # data = Order.objects.order_by('-placed_at')[:5].select_related('customer').prefetch_related('orderitem_set__product')

    # data = {
    # • How many orders do we have?
    # 'orders_count': Order.objects.aggregate(Count('id')),
    # • How many units of product 1 have we sold?
    # 'sold_product1': OrderItem.objects.filter(product_id=1, order__payment_status='C').aggregate(Sum('quantity')),
    # • How many orders has customer 1 placed?
    # 'c1_orders': Order.objects.filter(customer_id=1).aggregate(Count('id')),
    # • What is the min, max and average price of the products in collection 3?
    # 'min_max_avg': Product.objects.filter(collection_id=3).aggregate(Min('unit_price'), Max('unit_price'), Avg('unit_price'))
    # }

    # annotation challenge

    # data = {
    #     # Customers with their last order ID
    #     'customers': Customer.objects.annotate(last_order_id=Max('order__id')),
    #     # • Collections and count of their products
    #     'collections': Collection.objects.annotate(product_count=Count('product__id')),
    #     # • Customers with more than 5 orders
    #     'morethan5': Customer.objects.annotate(order_count=Count('order')).filter(order_count__gt=5),
    #     # • Customers and the total amount they’ve spent
    #     'spent': Customer.objects.annotate(amount_spent=Sum(F('order__orderitem__quantity') * F('order__orderitem__unit_price'), filter=Q(order__payment_status= 'C')))
    #     # • Top 5 best-selling products and their total sales

    # }

    # create a shopping cart with an item
    # cart = Cart.objects.create()
    # cart_item1 = CartItem.objects.create(quantity=2, cart=cart, product=Product(pk=3))
    # update the quantity of an item in a shopping cart
    # cartItem = CartItem.objects.filter(pk=6).update(quantity=1)
    # remove a shopping cart with its items
    # cart = Cart.objects.filter(pk=6).delete()

    return render(request, 'hello.html', data)
