from django.views.generic.list import ListView
from django.views import View
from .models import ProductsInfo


class ProductsInfoView(ListView):
    model = ProductsInfo
    template_name = 'goods_list.html'
    context_object_name = 'category'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsInfoView, self).get_context_data()
        context['site'] = self.request.site

        return context

    def get_queryset(self):
        items = ProductsInfo.on_site.all()  # фильтруем по сайтам
        return items


class ProductCategoryView(ListView, View):
    model = ProductsInfo
    template_name = 'category_goods_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCategoryView, self).get_context_data()
        context['title'] = 'категория/товары'
        context['all_products'] = ProductsInfo.on_site.all()

        return context

    def get_queryset(self):
        category_pk = self.kwargs['pk']
        return ProductsInfo.on_site.filter(category__pk=category_pk)
