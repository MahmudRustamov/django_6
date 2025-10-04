from django.urls import path
from . import views
from .views import ProductDetailView

app_name = 'products'


urlpatterns = [
    path('', views.product_filter_view, name='home'),
    path("filter/<str:filter_type>/<int:pk>/", views.product_filter_view, name="filter"),
    path('<int:pk>/', ProductDetailView.as_view(), name='detail'),
]