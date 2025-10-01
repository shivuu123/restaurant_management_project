import datetime

def is_restaurant_open():
    now = datetime.datetime.now()
    day = now.weekday()
    time = now.time()

    open_time, close_time = datetime.time(9, 0), datetime.time(22, 0)

    if day >= 5:
        open_time, close_time = datetime.time(10, 0), datetime.time(23, 0)

    return open_time <= time <= close_time