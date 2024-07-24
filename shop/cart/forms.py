from django import forms


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 100)]


class CartAddProductForm(forms.Form):
    # quantity = forms.CharField(label=False, attrs={'class': 'input_quant'})
    quantity = forms.IntegerField(
        min_value=1, initial=1, label=False, widget=forms.NumberInput(
            attrs={
                'class': 'form_quant',

            }
        )
    )
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput,
                                )





