"""Task 1"""

from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        current_date = datetime.today().date()
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        difference = (current_date - given_date).days
        return difference
    except ValueError:
        raise ValueError("Not correct date format. Please use 'YYYY-MM-DD'.")

print(get_days_from_today("2024-11-02"))
print(get_days_from_today("2024-12-12"))
print(get_days_from_today("24-12-12"))