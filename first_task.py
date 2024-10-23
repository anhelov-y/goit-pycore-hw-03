from datetime import datetime

# Введення дати та її перетворення у об"єкт datetime
date_string = input("Enter your date YYYY-MM-DD: ")
#Бескінечний цикл для перевірки вірності формату вводу даних
while True:
    try:
        date = datetime.strptime(date_string, "%Y-%m-%d")
    except Exception:                                                #ValueError 
        print("Incorrect format of date!")
        date_string = input("Enter your date Year-Month-Day: ")
    else:
        date = datetime.strptime(date_string, "%Y-%m-%d")  
        break      

# Функція розрахунку різниці дат
def get_days_from_today(date):
    now_time = datetime.today()
    days_since = now_time.toordinal() - date.toordinal()
    return days_since

print(get_days_from_today(date))
