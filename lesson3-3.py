
def sum_max_arg(*arg):
    c = arg[0]
    for i in arg:
        if i < c:
            c = i
    return sum(arg) - c

print(sum_max_arg(10, 5, 15))