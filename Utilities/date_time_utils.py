from datetime import date, timedelta


def return_today():
    today = date.today()
    today_day = today.strftime("%a %b %d %Y")
    return [today_day]


def return_tomorrow():
    tomorrow = date.today() + timedelta(days=1)
    tomorrow_day = tomorrow.strftime("%a %b %d %Y")
    return [tomorrow_day]


def return_current_week():
    today = date.today()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    start_day = start.strftime("%a %b %d %Y")
    end_day = end.strftime("%a %b %d %Y")
    return [start_day, end_day]


def return_next_week():
    next_week_today = date.today() + timedelta(days=6)
    start = next_week_today - timedelta(days=next_week_today.weekday())
    end = start + timedelta(days=6)
    start_day = start.strftime("%a %b %d %Y")
    end_day = end.strftime("%a %b %d %Y")
    return [start_day, end_day]


def return_current_month():
    today = date.today()
    start = today.replace(day=1)
    end = start.replace(
        month=start.month + 1,
        day=1
        ) - timedelta(days=1)
    start_day = start.strftime("%a %b %d %Y")
    end_day = end.strftime("%a %b %d %Y")
    return [start_day, end_day]


def return_next_month():
    today = date.today()
    start = today.replace(day=1, month=today.month + 1)
    end = start.replace(
        month=start.month + 1,
        day=1
        ) - timedelta(days=1)
    start_day = start.strftime("%a %b %d %Y")
    end_day = end.strftime("%a %b %d %Y")
    return [start_day, end_day]
