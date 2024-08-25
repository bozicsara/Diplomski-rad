from datetime import datetime, date, time


def get_date_by_timestamp(timestamp_date:float) -> date:
    return datetime.fromtimestamp(timestamp_date).date()


def get_time_by_timestamp(timestamp_date:float) -> time:
    return datetime.fromtimestamp(timestamp_date).time()