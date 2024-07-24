from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, PhotoSlider


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'image_show', 'price', 'discount', 'category']

    list_editable = ['price', 'category', 'discount']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['category']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return "None"

    image_show.__name__ = "Картинка"


@admin.register(PhotoSlider)
class SliderAdmin(admin.ModelAdmin):

    list_display = ['image_show']

    def image_show(self, obj):
        if obj.image:
            return mark_safe("<img src='{}' width='60' />".format(obj.image.url))
        return 'None'

    image_show.__name__ = 'Фото для слайда'