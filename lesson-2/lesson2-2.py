my_list = input('введите элементы массива через ",":')
my_list = my_list.split(',')
new_my_list = my_list.copy()
i = 1
if len(my_list) > 1:
    while i < len(my_list):
        new_my_list[i] = my_list[i-1]
        new_my_list[i-1] = my_list[i]
        i += 2
    if len(my_list) % 2 != 0:
        new_my_list[i-1] = my_list[i-1]
print(new_my_list)

