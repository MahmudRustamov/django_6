from django.urls import path
from apps.wishlist.views import wishlist_list, wishlist_add, wishlist_remove

app_name = 'wishlist'


urlpatterns = [
    path('', wishlist_list, name='list'),
    path('add/<int:product_id>/', wishlist_add, name='wishlist_add'),
    path('remove/<int:product_id>/', wishlist_remove, name='wishlist_remove'),
]
