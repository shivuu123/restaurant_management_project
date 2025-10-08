import datetime

def is_restaurant_open():
    now = datetime.datetime.now()
    day = now.weekday()
    time = now.time()

    open_time, close_time = datetime.time(9, 0), datetime.time(22, 0)

    if day >= 5:
        open_time, close_time = datetime.time(10, 0), datetime.time(23, 0)

    return open_time <= time <= close_time

def calculate_total_price(order_items):
    if not order_items:
        return 0.0
    return round(sum(item.get('quatity', 0) * item.get('price', 0) for item in order_items), 2)