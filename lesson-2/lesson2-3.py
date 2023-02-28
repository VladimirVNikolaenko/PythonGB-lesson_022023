month = input('Введите месяц числом:')
type_month = ['лето','осень','зима','весна']
if month == ('12' or '1' or '2'):
    print(type_month[2])
elif month == ('3' or '4' or '5'):
    print(type_month[3])
elif month == ('6' or '7' or '8'):
    print(type_month[0])
elif month == ('9' or '10' or '11'):
    print(type_month[1])

dict_month = {'12' : 'зима', '1' : 'зима', '2' : 'зима',
              '3' : 'весна',  '4' : 'весна', '5' : 'весна',
              '6' : 'лето',  '7' : 'лето', '8' : 'лето',
              '9' : 'осень',  '10' : 'осень', '11' : 'осень'}

for i in dict_month:
    if i == month:
        print(dict_month[i])