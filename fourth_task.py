from datetime import datetime, timedelta


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Andrew Williams", "birthday": "1998.10.30"},
    {"name": "Peter Parker", "birthday": "1998.11.5"},            #Додано для перевірки правильності відпрацювання функції
    {"name": "Superman Guy", "birthday": "1998.10.27"},
    {"name": "Man like a Joke", "birthday": "1998.10.26"}
]

now_time = datetime.today().date()
#Загальна функція для перевірки дат
def get_upcoming_birthdays(num):
    new_dict = []                                                                           #Пустий список для запису дат відповідно до умови (не пізніше 7 днів від сьогодні)
    for user in users:                                                                      # Зміна формату дат та року
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_this_year.replace(now_time.year)
        if birthday_this_year < now_time:                                                   #Перевірка умови чи задана дата вже минула
            pass
        else:                                                                               #Розрахунок різниці дат не включаючи минулі
            days_since = birthday_this_year.toordinal() - now_time.toordinal()
            if days_since > 7:                                                              #Виключення дат > 7днів вперед
                pass
            else:                                                                           #Створення словника для запису в нього необхідних ключ-значень з правильними датами
                new_list = {}                                                               
                new_list["name"]= user["name"]                                            
                day_of_week = birthday_this_year.isoweekday()                               #Перевіряємо якому дню тижня відповідає кожна дата, яка пройшла попередні умови  
                if day_of_week == 6:                                                        #(6,7 - вихідні дні) - відповідно додаємо 1-2 дні щоб дата перенеслась на понеділок 
                    birthday_this_year = birthday_this_year + timedelta(days=2)
                    new_list["birthday"] = birthday_this_year.strftime("%Y.%m.%d")
                    new_dict.append(new_list)
                elif day_of_week == 7:
                    birthday_this_year = birthday_this_year + timedelta(days=1)
                    new_list["birthday"] = birthday_this_year.strftime("%Y.%m.%d")
                    new_dict.append(new_list) 
                else:                                                                       #Якщо дата(день) != вихідний, то просто передаємо дату з ключем у список
                    new_list["birthday"] = birthday_this_year.strftime("%Y.%m.%d")
                    new_dict.append(new_list) 
    return new_dict                                                                         #Повертаємо список з ключами-значеннями необхідних нам дат


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)