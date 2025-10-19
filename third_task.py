import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
#Оголошуємо функцію для перевірки префікса у кожному номері (+), (38), відсутність та додаємо необхідний префікс
def check_prefix(num):                              
    if num.startswith("+"):
        pass
    elif num.startswith("38"):
        num = "+" + num
    else:
        num = "+38" + num
    return num
#Оголошуємо функцію для видалення усіх зайвих знаків окрім цифр
def normalize_phone(num):
    pattern = re.compile(r"[^0-9+]")
    replacement = r""
    num = re.sub(pattern,replacement,num)
    return check_prefix(num)

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)