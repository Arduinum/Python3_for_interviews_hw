from django.urls import path
from .views import ProductsInfoView, ProductCategoryView

urlpatterns = [
    path('', ProductsInfoView.as_view(), name='goods_list'),
    path('category/products/<int:pk>/', ProductCategoryView.as_view(), name='category_goods_list')
]
