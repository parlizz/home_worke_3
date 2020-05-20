def int_func(text):
    return text.title()


def func(text):
    listed_text = list(text)
    listed_text[0] = listed_text[0].upper()
    return ''.join(listed_text)


out_1 = []
out_2 = []
for word in input('Введите слова разделенные пробелом: ').split(' '):
    out_1.append(int_func(word))
    out_2.append(func(word))

print(f'Вариант1: {" ".join(out_1)}')
print(f'Вариант2: {" ".join(out_2)}')
