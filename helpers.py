import datetime

class DataDay:
    today = datetime.date.today()
    tomorrow = today + datetime.timedelta(days=1)

    delivery_day_today = today.strftime('%d')
    delivery_day_tomorrow = tomorrow.strftime('%d')