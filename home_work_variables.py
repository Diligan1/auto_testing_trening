﻿# Задание 1: Конвертация Температуры

# Исходная температура в Цельсиях
grades_celsius = 37

# Через формулу конвертируем градусы в форенгейты
convertation_fahrenheit = grades_celsius * 9 / 5 + 32

# Выводим результат
print(f'Грудусы Цельсия: {grades_celsius}°C = Градусы Фаренгейта: {convertation_fahrenheit}°F')

# ДОПОЛНИТЕЛЬНОЕ РЕШЕНИЕ 1 :

# Создаем переменную и присваеваем ей функцию input, которая принимает в себя целые числа
grades_celsius = int(input('Введите градусы цельсия:'))

# Выводим на экран результат ввода градусов
print('Градусы Фаренгейта', grades_celsius * 9 / 5 + 32)


# ДОПОЛНИТЕЛЬНОЕ РЕШЕНИЕ 2 :

# Создаем функцию, которая выполняет в себе формулу
def gradus(a):
    return (a * 9 / 5) + 32


# Выводим результат с аргументом
print('Градусы Фаренгейта:', gradus(37))

# Задание 2: Подсчет Среднего Значения

# Cоздаем переменные с числами
num_one = 20
num_two = 20
num_three = 45

# Считаем сумму перемменных и делим их на 3
average = (num_one + num_two + num_three) / 3
# Выводим результат
print(f'Среднее значение: {average}')


# ДОПОЛНИТЕЛЬНОЕ РЕШЕНИЕ 1 :

# Создаем функцию и присваиваем ей параметры
def average(a, b, c):
    # Возвращаем результат сложение параметров между собой
    return (a + b + c) / 3


# Выводим на экран аргументы
print('Среднее значение:', average(20, 20, 45))

# ДОПОЛНИТЕЛЬНОЕ РЕШЕНИЕ 2 :

# Создаем кортеж с тремя элементами
numbers = (20, 20, 45)

# сумму(sum) значений делим на длинну(len) значений в кортеже и выводим результат
print('Среднее значение:', sum(numbers) / len(numbers))

# Задание 3: Проверка Четности Числа

# Переменной присваиваем функцию ввода, которая принимает в себя целые числа
number = int(input('Введите число:'))

# C помощью условия проверяем число на четность
if number % 2 == 0:
    print(f'Число {number}: четное')
else:
    print(f'Число {number}: нечетное')
