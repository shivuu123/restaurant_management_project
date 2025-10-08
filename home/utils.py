def calculate_total_price(order_items):
    if not order_items:
        return 0.0
    return round(sum(item.get('quatity', 0) * item.get('price', 0) for item in order_items), 2)