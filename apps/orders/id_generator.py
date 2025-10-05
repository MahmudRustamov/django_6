import secrets
from apps.orders.models import OrderModel

ALPHABET = "ABCDEFGHJKLMNPQRSTUVWXYZ1234567890"
ORDER_ID_LENGTH = 10

def make_order_id(length=ORDER_ID_LENGTH):
    """Generate a unique order ID that does not already exist in the database."""
    while True:
        order_id = ''.join(secrets.choice(ALPHABET) for _ in range(length))
        if not OrderModel.objects.filter(unique_id=order_id).exists():
            return order_id
