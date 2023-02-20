text = True

while text:
    try:
        a = int(input('Введите число a:'))
        b = int(input('Введите число b:'))
        text = False
    except Exception:
        print('Введите число')
        text = True


def diff(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        print('Невозможно выполнить деление на 0')


print(diff(a, b))



