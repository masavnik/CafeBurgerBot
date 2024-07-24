from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'first_last_name', 'user_tg', 'phone',
                    'address', 'created', 'updated', 'comment', 'payment_method', 'delivery_method']
    list_filter = ['created', 'updated']



admin.site.register(Order, OrderAdmin)
