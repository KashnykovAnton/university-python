"""Task 4"""

from datetime import datetime

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        difference = (birthday_this_year - today).days
        if difference <= 7:
            weekday = birthday_this_year.weekday()
            if weekday == 5:
                birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day + 2)
            elif weekday == 6:
                birthday_this_year = birthday_this_year.replace(day=birthday_this_year.day + 1)
             upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
            })
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "David Black", "birthday": "1995.12.04"},
    {"name": "Ann White", "birthday": "1991.12.07"}, # 2024.12.07 - Saturday, congrats on Monday 2025.12.09
    {"name": "Dennis Green", "birthday": "1998.12.08"}, # 2024.12.08 - Sunday, congrats on Monday 2025.12.09
    {"name": "Peter Brown", "birthday": "2001.12.01"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)