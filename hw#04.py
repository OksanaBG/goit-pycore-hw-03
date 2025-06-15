from datetime import datetime, timedelta
def get_upcoming_birthdays(users):
    # upcoming list
    upcoming_birthdays=[]
    today=datetime.today().date()
    this_week = today + timedelta(days=7)
    #cheсk user`s bithday
    for user in users:
        try:
            birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        except ValueError:
            continue

        birthday_this_year=birthday.replace(year=today.year)
        # cheсk if BD pass
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        # cheсk if BD in next 7 days
        if today <= birthday_this_year <= this_week:
            congratulation_date = birthday_this_year

            # cheсking if BD on weekend
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # add BD to upcoming list
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays
#testing list of users
users = [
    {"name": "John Doe", "birthday": "1985.06.10"},
    {"name": "Jane Smith", "birthday": "1990.06.15"},
    {"name": "Ivan Petrov", "birthday": "1980.06.16"},
    {"name": "Oksana Ivanenko", "birthday": "1992.06.08"},
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)