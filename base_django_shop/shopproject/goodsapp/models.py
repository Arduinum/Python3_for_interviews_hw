from django.db import models
from django.contrib.sites.models import Site
from django.contrib.sites.managers import CurrentSiteManager


class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='название',
        max_length=255,
        unique=True
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        null=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name or f'Category with id - {self.pk}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class ProductsInfo(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        verbose_name='категория'
    )

    name = models.CharField(
        verbose_name='название',
        max_length=255,
        unique=True
    )

    price = models.DecimalField(
        verbose_name='цена',
        max_digits=8,
        decimal_places=2,
        default=0
    )

    measure = models.CharField(
        verbose_name='еденица измерения',
        max_length=4
    )

    quantity = models.PositiveIntegerField(
        verbose_name='колличество товара на складе',
        default=0
    )

    name_provider = models.CharField(
        verbose_name='название поставщика',
        max_length=255
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.CASCADE,
        null=True
    )

    objects = models.Manager()

    # будет автоматом фильтровать модели по привязки к сайтам
    on_site = CurrentSiteManager(
        'site'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        auto_created=True
    )

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name or f'Product width id - {self.pk}'

    class Meta:
        verbose_name = 'карточка товаров'
        verbose_name_plural = 'карточки товаров'
