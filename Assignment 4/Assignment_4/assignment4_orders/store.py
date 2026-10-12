from models import Order

_orders: dict[int, Order] = {}
_by_key: dict[str, int] = {}
_next_id = 1

def reserve_id():
    global _next_id
    order_id = _next_id
    _next_id += 1
    return order_id

def create(user_id, item_id, quantity, amount, status, payment_id, key=None, order_id=None):
    if order_id is None:
        order_id = reserve_id()
    order = Order(
        id=order_id,
        user_id=user_id,
        item_id=item_id,
        quantity=quantity,
        amount=amount,
        status=status,
        payment_id=payment_id,
        idempotency_key=key,
    )
    _orders[order.id] = order
    if key:
        _by_key[key] = order.id
    return order

def find(order_id):
    return _orders.get(order_id)

def find_by_key(key):
    return _orders.get(_by_key.get(key))

def find_by_filter(user_id=None, status=None):
    result = list(_orders.values())
    if user_id is not None:
        result = [o for o in result if o.user_id == user_id]
    if status is not None:
        result = [o for o in result if o.status == status]
    return result

def reset():
    global _orders, _by_key, _next_id
    _orders = {}
    _by_key = {}
    _next_id = 1
