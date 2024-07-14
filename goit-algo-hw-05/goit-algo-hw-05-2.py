import re
from typing import Callable

def generator_numbers(text: str):
    pattern = re.compile(r'\b\d+\b')
    matches = pattern.findall(text)
    for match in matches:
        yield int(match)

def sum_profit(text: str, func: Callable):
    total = 0
    for number in func(text):
        total += number
    return total


text = "Alex Korp, 3000 Nikita Borisenko, 2000 Sitarama Raju, 1000"
print(sum_profit(text, generator_numbers))