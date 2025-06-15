from datetime import datetime
def get_date(string):
    try:
        input_date=datetime.strptime(string, "%Y-%m-%d").date()
        return input_date
    except ValueError:
        print ("Input format error")
        return None

def get_days_from_today(input_date):
    today=datetime.today().date()
    delta_days=today-input_date
    delta_days=delta_days.days
    return delta_days

###---------####
input_date= get_date(str(input("Please, insert data in format YYYY-MM-DD:>>> ")))
if input_date:
    print(get_days_from_today(input_date))
else:
    print ("Something wrong")