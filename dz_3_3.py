def my_func(arg_1, arg_2, arg_3):
    print(f'Сумма двух наибольших аргументов равна: {arg_1 + arg_2 + arg_3 - min([arg_1, arg_2, arg_3])}')


my_func(
    int(input('аргумент 1: ')),
    int(input('аргумент 2: ')),
    int(input('аргумент 3: ')),
)