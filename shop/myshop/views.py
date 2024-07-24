from django.shortcuts import render, get_object_or_404
from .models import Category, Product, PhotoSlider
from cart.forms import CartAddProductForm


def delivery_view(request):
    return render(request, 'myshop/product/delivery.html')


def about_pay_view(request):
    return render(request, 'myshop/product/about_pay.html')


def contact_view(request):
    return render(request, 'myshop/product/contact.html')


def reviews_view(request):
    return render(request, 'myshop/product/reviews.html')


def network_view(request):
    return render(request, 'myshop/product/network.html')


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()
    photo_slider = PhotoSlider.objects.all()
    cart_product_form = CartAddProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'myshop/product/product_list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products,
                      'photo_slider': photo_slider,
                      'cart_product_form': cart_product_form,
                  })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'myshop/product/product_detail.html', {'product': product,
                                                                  'cart_product_form': cart_product_form,
                                                                  })
