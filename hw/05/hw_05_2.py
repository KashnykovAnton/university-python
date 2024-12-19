import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r"\s(\d+\.\d+)\s"
    matches = re.findall(pattern, f" {text} ")
    
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))

text = "Загальний дохід працівника: 1000.01 основний, 27.45 бонус, і 324.00 додаткові доходи."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}") # Виведе "Загальний дохід: 1351.46"
