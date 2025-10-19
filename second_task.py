import random

#Введення чисел (умови) для вибірки
min = int(input("Enter MIN number: "))
max = int(input("Enter MAX number: "))
quantity = int(input("Enter Quantity of numbers: "))

#Функція з перевіркою чисел та розрахунком
def get_numbers_ticket(min, max, quantity):
    # Перевірка заданих чисел min, max, quantity
    if min < 1:
        return ("[       ]")
    if max > 1000:
        return ("[       ]")
    if max-min < quantity: 
        return ("[       ]")
    # Обчислення і сортування
    population = range(min,max)
    lottery_numbers=random.sample(population, quantity)
    lottery_numbers.sort()
    return lottery_numbers

lottery_numbers = get_numbers_ticket(min, max, quantity)
print(lottery_numbers)