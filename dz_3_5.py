def calculate(*nums):
    sum = 0
    stop = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            stop = True
    return sum, stop


g_sum = 0

while True:
    numbers = input('Введите числа через пробел: ').split(' ')
    sum, stop_flag = calculate(*numbers)
    g_sum += sum
    print(f'сумма {g_sum}')

    if stop_flag:
        break
