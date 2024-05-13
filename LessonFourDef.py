# ФУНКЦИИ
result = len('Hello!')  # функция len считает количество символов в строке и т.д
print(result)


def great(name):
    print('Hello, ' + name + "!")


great('Ilya')
great('Alena')


def ilya(a, b):
    result1 = a + b
    return result1



be = ilya(2, 8)
b1 = ilya(10, 100)
b2 = ilya(1000, 200)
print(be,b1,b2)


# пример работы встроенной функции

result = len('Hello world')
print(result)

result = pow(10, 2)
print(result)


