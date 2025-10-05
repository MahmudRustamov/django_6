from django.db import models

from django.contrib.auth import get_user_model

from apps.pages.models import BaseModel
from apps.products.models import ProductModel

User = get_user_model()

class WishlistModel(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="wishlist_items")
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="wishlisted_by")

    class Meta:
        verbose_name = "wishlist"
        verbose_name_plural = "wishlists"

    def __str__(self):
        return f"{self.user.username} → {self.product.title}"
