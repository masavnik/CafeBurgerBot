from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/photos_categories/', blank=True, verbose_name='Фото категории')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='category',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True, verbose_name='Названия')
    slug = models.CharField(max_length=150, db_index=True, unique=True, verbose_name='Ссылка')
    description = models.TextField(max_length=1000, blank=True, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='media/photos_product/', blank=True, verbose_name='Фото')
    discount = models.IntegerField(verbose_name='Скидка(Сумма)', blank=True, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])

    def get_discounted_price(self):
        return self.price - self.discount

class PhotoSlider(models.Model):
    image = models.ImageField(upload_to='media/photos_slider/', verbose_name='Фото')

    def __str__(self):
        return str(self.image)

    class Meta:
        verbose_name_plural = 'Фото для слайда'
        verbose_name = 'Фото для слайда'