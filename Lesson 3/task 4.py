def my_func(x, y):
    z = 1 / x ** y
    print(f'{z}')


my_func(4, 8)

def my_func(x, y):
    z = 1
    for i in range(abs(y)):
        z *= x
    if y >= 0:
        return z
    else:
        return 1 / z


print(my_func(4, -8))
