import datetime

def get_days_from_today(date):
    try:
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.date.today()
        difference = today - date_obj
        return difference.days
    except ValueError:
        return "Неправильний формат дати."
    
print(get_days_from_today("2024-05-30"))

import random

def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= 1000) or not (1 <= max <= 1000) or not (min <= max) or not (min <= quantity <= max - min + 1):
        return []
    numbers = random.sample(range(min, max + 1), quantity)
    numbers.sort()
    return numbers

print(get_numbers_ticket(1,100,5))
