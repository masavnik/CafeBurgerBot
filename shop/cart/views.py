from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from myshop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 update_quantity=cd['update'],
                 quantity=cd['quantity'])
    return redirect('myshop:product_list')


def clear_cart(request):
    # Очистка сессии корзины
    request.session['cart'] = {}
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    count_product = len(cart)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
                                                                   'update': True})

    return render(request, 'cart/detail.html', {'cart': cart,
                                                'count_product': count_product})
