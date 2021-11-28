from django.urls import path
from .views import ProductsInfoView

urlpatterns = [
    path('', ProductsInfoView.as_view())
]
