# Словари, коллекция пар ключ-значение, изменяемая.

# Получение значение по ключу

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['age'])  # выводит значение возраста

# Добавление новой пары ключ-значение

my_dict['job'] = 'Developer'  # добавляем новую пару ключ-значение
print(my_dict)

# Удаление элемента из словаря
del my_dict['city']
print(my_dict)