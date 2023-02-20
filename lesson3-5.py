# Спец. символ "!"

switch = False
gl_my_sum = 0


def my_func(*arg):
    my_sum = 0
    for i in arg:
        if i == '!':
            global switch
            switch = True
            break
        else:
            my_sum += int(i)
    return my_sum


while not switch:
    my_array = input('Введите строку чисел разделенных пробелом:').split(' ')
    gl_my_sum += my_func(*my_array)
    print(gl_my_sum)


