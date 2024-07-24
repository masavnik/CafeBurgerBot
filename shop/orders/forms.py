from django import forms
from django.forms import RadioSelect

from .models import Order


class OrderCreateForm(forms.ModelForm):
    payment_method = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Order.CHOICES_PAY,
        label="Оплата"
    )

    delivery_method = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=Order.CHOICES_DELIVERY,
        label="Доставка"
    )

    class Meta:
        model = Order
        fields = ['first_last_name', 'phone', 'address', 'comment', 'user_tg', 'delivery_method', 'payment_method']
        widgets = {'comment': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 340px; height: 80px;',
                                                     'placeholder': 'Введите комментарий к заказу'}),
                   'first_last_name': forms.TextInput(
                       attrs={'class': 'name_user', 'placeholder': 'Введите имя и фамилию'}),
                   'phone': forms.TextInput(attrs={'class': 'phone_user', 'placeholder': 'Введите номер телефона'}),
                   'address': forms.TextInput(attrs={'class': 'address', 'placeholder': 'Введите адрес доставки'}),
                   'user_tg': forms.TextInput(
                       attrs={'class': 'address', 'placeholder': 'Введите ваше имя пользователя в Telegram'})}
