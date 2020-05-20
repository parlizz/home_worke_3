# 2. Реализовать функцию, принимающую несколько параметров, описывающих 
# данные пользователя: имя, фамилия, год рождения, город проживания, email, 
# телефон. Функция должна принимать параметры как именованные аргументы. 
# Реализовать вывод данных о пользователе одной строкой.

def person(name, lastname, birthday, city, email, phone):
    return print(f'Имя: {name}; Фамилия: {lastname}; Год рождения: {birthday};'
                 f' Город проживания: {city}; Email: {email}; Телефон: {phone}.')


person(
    name=input('Имя: '),
    lastname=input('Фамилия: '),
    birthday=input('Год рождения: '),
    city=input('Город проживания: '),
    email=input('Email: '),
    phone=input('Телефон: '),
)
