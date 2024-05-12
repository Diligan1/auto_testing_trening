# Cловари - {} dict

my_dict = {"numbers": "one", "fruits": "banana", "name": "igor"}  # словари предоставляют собой некий набор "ключ":
# "значение
print('Вывод словаря на печать:', my_dict)

# Работа со словарями
value = my_dict['numbers']  # через индексацию [] мы можем получить значения определеннного ключа
print('Выводит значение указаного ключа numbers:', value)

my_dict["auto"] = "bmw"  # добавление элементов в существующий словарь
print('В данном случае добавится новая пара ключ и значения :', my_dict)

my_dict["numbers"] = "two"  # изменение существующего значения через ключ
print('В ключе numbers изменили one на :', my_dict)

del my_dict["fruits"]  # удаление элемента из словаря с помощью ключа
print('Элемент fruits был удаление из словаря:', my_dict)

# Методы работы со словарями

keys = my_dict.keys()  # с помощью метода .keys() получаем все ключи
print('Вывод только ключей:', keys)

keys = my_dict.values()  # с помощью метода values() получаем только значения
print('Вывод только значений:', keys)

keys = my_dict.items()  # с помощью метода items() мы можем получить все элементы в виде кортежей
print(keys)

value = my_dict.get("name")  # с помощью метода get() можно получить значение по ключу
print(value)

# Итерация элементов с помошью цикла For

# Итерация только по ключу
for key in my_dict.keys():  # С помощью метода keyes() мы получаем только ключи в словаре и цикл for итерирует каждый
    # элемент
    print(f'Вывод только ключей: {key}')

# Итерация только по значению
for values in my_dict.values():  # С помощью метода values() мы получаем только значения в словаре и цикл for
    # итерирует каждый
    # элемент

    print(f'Вывод только значений:{values}')

# Итерация по парам ключ-значение:
for key, value in my_dict.items():  # в данном случае с помощью метода items мы получаем все элементы в словаре и
    # итерируемых их с помощью цикла for
    print(f'{key} : {value}')  # через f строку мы выводим ключ и значения словаря

# Обновление элементов в словаре

update_dict = my_dict.update({"auto": "mercedes"})
print(update_dict)
