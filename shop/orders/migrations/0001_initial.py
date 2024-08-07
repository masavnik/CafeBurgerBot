# Generated by Django 4.0 on 2024-07-22 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_last_name', models.CharField(max_length=50, verbose_name='Имя Фамилия')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес доставки')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('comment', models.CharField(max_length=200, verbose_name='Комментарий к заказу')),
                ('user_tg', models.CharField(max_length=200, verbose_name='Ваше имя пользователя в Telegram')),
                ('payment_method', models.CharField(choices=[('bank_transfer', 'Оплата по реквизитам'), ('cash_on_delivery', 'Наличными при получении')], max_length=20, verbose_name='Оплата')),
                ('delivery_method', models.CharField(choices=[('pickup', 'Доставка'), ('delivery', 'Самовывоз')], max_length=20, verbose_name='Доставка')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='myshop.product')),
            ],
        ),
    ]
