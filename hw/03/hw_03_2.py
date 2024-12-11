"""Task 2"""

import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list[int]:
    if min < 1:
        print("min number should be 1 or more")
        return []
    if max > 1000:
        print("max number should be 1000 or less")
        return []
    if not (min < quantity < max):
        print("quantity should be between min and max")
        return []
    return random.sample(range(min, max + 1), quantity)


print(get_numbers_ticket(1, 100, 5))
print(get_numbers_ticket(0, 100, 5))
print(get_numbers_ticket(1, 1001, 5))
print(get_numbers_ticket(1, 100, 500))