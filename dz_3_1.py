# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и 
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть 
# обработку ситуации деления на ноль.

def my_func(arg_1, arg_2):
    try:
        return arg_1 / arg_2
    except ZeroDivisionError as e:
        print(f'деление на 0!')


print(my_func(int(input('введите первое число:')), int(input('введите второе число:'))))

