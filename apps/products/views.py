from django.shortcuts import render


def products_list_view(request):
    return render(request, 'products/product-grid-sidebar-left.html')


def product_detail_veiw(request):
    return render(request, 'products/product-checkout.html')