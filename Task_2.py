import random 
def get_numbers_ticket(min, max, quantity):
    if not (1 <= min <= max <= 1000) or not (min <= quantity <= max):       # Перевірка валідності параметрів згідно з умовами
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)  # генерує унікальні випадкові числа в діапазоні від min до max включно, кількість яких дорівнює quantity
    
    return sorted(numbers)   # Повертаємо відсортований список

print(f"Лотерейні числа: {get_numbers_ticket(1, 1000, 5)}")   # Приклад виклику функції

