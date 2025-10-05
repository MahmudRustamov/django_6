from django.contrib import admin
from django.contrib import admin
from .models import OrderModel, OrderItemModel


class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 0
    readonly_fields = ('product', 'quantity', 'price')
    can_delete = False


@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'unique_id', 'total_price', 'total_products', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__full_name', 'unique_id')
    readonly_fields = ('unique_id', 'user', 'total_price', 'total_products', 'created_at', 'updated_at')
    inlines = [OrderItemInline]

    def has_add_permission(self, request):
        return False


@admin.register(OrderItemModel)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    readonly_fields = ('order', 'product', 'quantity', 'price', 'created_at', 'updated_at')
    search_fields = ('order__unique_id', 'product__title')

