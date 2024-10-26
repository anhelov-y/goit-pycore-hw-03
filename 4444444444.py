from datetime import datetime, timedelta


users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Andrew Williams", "birthday": "1998.10.30"},
    {"name": "Peter Parker", "birthday": "1998.11.5"},
    {"name": "Superman Guy", "birthday": "1998.10.27"},
    {"name": "Man like a Joke", "birthday": "1998.10.26"}
]

now_time = datetime.today().date()


def get_upcoming_birthdays(num):
    new_dict = []
    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_this_year.replace(now_time.year)
        if birthday_this_year < now_time:
            pass
        else:
            days_since = birthday_this_year.toordinal() - now_time.toordinal()
            if days_since > 7:
                pass
            else:    
                new_list = {}                                                               
                new_list["name"]= user["name"]                                            
                day_of_week = birthday_this_year.isoweekday()
                if day_of_week == 6:
                    birthday_this_year = birthday_this_year + timedelta(days=2)
                    new_list["birthday"] = birthday_this_year.strftime("%Y.%m.%d")
                    new_dict.append(new_list)
                elif day_of_week == 7:
                    birthday_this_year = birthday_this_year + timedelta(days=1)
                    new_list["birthday"] = birthday_this_year.strftime("%Y.%m.%d")
                    new_dict.append(new_list) 
                else:
                    new_list["birthday"] = birthday_this_year.strftime("%Y.%m.%d")
                    new_dict.append(new_list) 
    return new_dict


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)