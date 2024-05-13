# Задание 1: Определение Времени Года

# Переменной присваиваем функцию input(), которая принимает в себя целые значения, запрос месяца
month = int(input('Введите номер месяца:'))
if month == 12 or month == 2:
    print(f'Месяц под номером -\t{month}: Зима')
elif month == 3 or month == 5:
    print(f'Месяц под номером -\t{month}: Весна')
elif month == 6 or month == 8:
    print(f'Месяц под номером -\t{month}: Лето')
elif month == 9 or month == 11:
    print(f'Месяц под номером -\t{month}: Осень')
else:
    print(f'К сожалению, времени года под номером -\t{month}: Не существует.\nВведите корректный месяц: от 1 до 12.')

# Задание 2: Ранг пользователя

# Запрос кол-во очков
level = int(input('Введите количество очков:'))
if level < 1000:
    print(f'Ваш Уровень {level}: Новичок')
elif level < 5000:
    print(f'Ваш Уровень {level}: Любитель')
else:
    print(f'Ваш Уровень {level}: Мастер')

# Задание 3: Скидка за покупку

# Запрос суммы покупки
price = float(input("Введите сумму покупки: "))

# Определение скидки
if price > 2000:
    discount_price = price * 0.1
elif price >= 1000:
    discount_price = price * 0.05
else:
    discount_price = 0
# Расчет суммы с учетом скидки
result = price - discount_price
# Вывод результата
print(f"Сумма к оплате с учетом скидки: {result} руб.")
