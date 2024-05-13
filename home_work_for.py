# Задание 1: Вывод четных чисел

num = int(input('Ввведите число:'))
for numbers in range(1, num + 1):
    if numbers % 2 == 0:
        print('Число четное:', numbers)

# Задание 2: Подсчет количества цифр

# Получаем ввод пользователя
num = int(input("Введите целое число: "))

# Создаем переменную для хранения количества цифр
digit_count = 0

# Цикл для перебора цифр в числе
for digit in str(num):
    digit_count += 1
# Вывод результат
print("Количество цифр в числе:", digit_count)

# Задание 3: Сумма чисел в строке
num_string = input("Введите число с пробелом: ")

# Убираем пробелы из введенных данных
num_list = num_string.split()
# Создаем переменную для хранения чисел
sum_str = 0
# Цикл для подсчета чисел
for num_sum in num_list:
    sum_str += int(num_sum)
print(f'Cумма чисел: {sum_str}')
