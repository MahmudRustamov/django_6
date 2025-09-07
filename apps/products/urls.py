from django.urls import path
from apps.products.views import products_list_view, product_detail_veiw

app_name = 'products'


urlpatterns = [
    path('', products_list_view, name='products'),
    path('detail/', product_detail_veiw, name='product_detail'),
]