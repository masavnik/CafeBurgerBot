from django.db import models
from myshop.models import Product
from django.urls import reverse


class Order(models.Model):
    CHOICES_PAY = [
        ('bank_transfer', 'Оплата по реквизитам'),
        ('cash_on_delivery', 'Наличными при получении'),
    ]

    CHOICES_DELIVERY = [
        ('pickup', 'Доставка'),
        ('delivery', 'Самовывоз'),
    ]

    first_last_name = models.CharField(max_length=50, verbose_name='Имя Фамилия')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=250, verbose_name='Адрес доставки')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = models.CharField(max_length=200, verbose_name='Комментарий к заказу')
    user_tg = models.CharField(max_length=200, verbose_name='Имя телеграм')
    payment_method = models.CharField(max_length=20, choices=CHOICES_PAY, verbose_name='Оплата')
    delivery_method = models.CharField(max_length=20, choices=CHOICES_DELIVERY, verbose_name='Доставка')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id, self.first_last_name)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id, self.product)

    def get_cost(self):
        return self.price * self.quantity
