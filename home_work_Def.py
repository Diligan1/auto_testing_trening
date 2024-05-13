def convert_celsius_to_fahrenheit(gradus_celsion):
    fahrenheit = (gradus_celsion * 9 / 5) + 32
    return fahrenheit


celsius = float(input("Введите температуру в градусах Цельсия: "))
# В функцию положили ввод температуры
fahrenheit = convert_celsius_to_fahrenheit(celsius)
print("Температура в градусах Фаренгейта:", fahrenheit, "°F")
