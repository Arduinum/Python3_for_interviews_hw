from django.views.generic.list import ListView
from django.views import View
from .models import ProductsInfo


def get_tags_list():
    tags_list = list(ProductsInfo.objects.select_related('category').values('tags'))
    tags = set()
    for t in tags_list:
        for tag in t['tags'].split(', '):
            tags.add(tag)

    return list(tags)


class ProductsInfoView(ListView):
    model = ProductsInfo
    template_name = 'goods_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsInfoView, self).get_context_data()
        context['title'] = 'все_товары'
        context['tags'] = get_tags_list()

        return context

    def get_queryset(self):
        items = ProductsInfo.objects.select_related('category')
        return items


class ProductCategoryView(ListView, View):
    model = ProductsInfo
    template_name = 'category_goods_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryView, self).get_context_data()
        context['title'] = 'категория/товары'
        context['all_products'] = ProductsInfo.objects.select_related('category')
        context['tags'] = get_tags_list()

        return context

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return ProductsInfo.objects.select_related('category').filter(category__pk=category_pk)
