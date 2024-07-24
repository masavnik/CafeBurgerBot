from django.urls import path
from . import views

app_name = 'myshop'

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('delivery/', views.delivery_view, name='delivery'),
    path('about_pay/', views.about_pay_view, name='about_pay'),
    path('contact/', views.contact_view, name='contact'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('network/', views.network_view, name='network'),

    path('<slug:category_slug>/', views.product_list,
         name='product_list_by_category'
         ),
    path('<int:id>/<slug:slug>', views.product_detail,
         name='product_detail'),

]
