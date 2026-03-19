from datetime import datetime

def get_days_from_today(date):
    try:
        converted_date = datetime.strptime(date, "%Y-%m-%d").date()   # Перетворення рядка у об'єкт date
        date_today = datetime.today().date()   # Отримання поточної дати
        delta = converted_date - date_today  # Різниця між введеною датою та поточною датою
        return delta.days  # Повернення кількості днів
    except ValueError:    
        print("Invalid date format. Please use YYYY-MM-DD.")        
        return None      
    print(f"Різниця у днях: {get_days_from_today('2026-03-19')}")  # Виведення результату для прикладу дати "2026-03-19"