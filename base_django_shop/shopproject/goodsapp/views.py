from django.views.generic.list import ListView
from .models import ProductsInfo


class ProductsInfoView(ListView):
    model = ProductsInfo
    template_name = 'goods_list.html'

    def get_queryset(self):
        items = ProductsInfo.objects.all()
        return items
