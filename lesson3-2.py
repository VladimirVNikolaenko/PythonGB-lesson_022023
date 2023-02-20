

def user_data(**params):
    return params.values()


print(user_data(u_name='Ivan', u_last_name='Ivanov', u_b_day='1990',
                u_city='Moscow', u_email='IIvanov@test.com', u_phone='+79001231234'))
