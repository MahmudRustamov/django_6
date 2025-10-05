from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from apps.products.models import ProductModel
from apps.wishlist.models import WishlistModel


@login_required
def wishlist_add(request, product_id):
    """Mahsulotni foydalanuvchi wishlistiga qo‘shadi"""
    product = get_object_or_404(ProductModel, id=product_id)
    WishlistModel.objects.get_or_create(user=request.user, product=product)
    return redirect(request.META.get('HTTP_REFERER', 'wishlist:list'))


@login_required
def wishlist_remove(request, product_id):
    """Wishlistdan mahsulotni o‘chiradi"""
    product = get_object_or_404(ProductModel, id=product_id)
    WishlistModel.objects.filter(user=request.user, product=product).delete()
    return redirect(request.META.get('HTTP_REFERER', 'wishlist:list'))


@login_required
def wishlist_list(request):
    """Foydalanuvchining wishlistini ko‘rsatadi"""
    items = WishlistModel.objects.filter(user=request.user).select_related('product')
    return render(request, 'auth/user-wishlist.html', {'items': items})


def in_wishlist(self, product_id):
    return str(product_id) in self.basket.keys()
