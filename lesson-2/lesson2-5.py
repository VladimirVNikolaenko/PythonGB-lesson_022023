item = input('Ведите целое число:')
my_list = [7, 5, 3, 3, 2]
my_index = 0
ii = 0
for i in my_list:
    if i > int(item):
        my_index = ii
    elif i <= int(item) and my_index > 0:
        my_index = ii
        break
    else:
        my_index = 0
    ii += 1

if my_index == ii-1:
    my_index += 1

my_list.insert(my_index, item)
print(my_list)
