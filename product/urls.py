
from django.urls import path
from .views import list_product, list_product_price, product_add_with_html
#major first 
urlpatterns = [
    path('view/',list_product),
    path('list_product_price/',list_product_price),
    path('product_add_with_html/',product_add_with_html)
]
