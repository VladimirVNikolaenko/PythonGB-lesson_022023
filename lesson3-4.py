x = int(input('Введите целое пложительное число:'))
y = int(input('Введите целое отрицательное число:'))

while x <= 0 or y >= 0:
    x = int(input('Введите целое пложительное число:'))
    y = int(input('Введите целое отрицательное число:'))


def my_func(a, b):
    return a ** b


print(my_func(x, y))
