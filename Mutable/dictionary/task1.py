#1
#Напишите программу, которая получает на вход название книги - title,
#фамилию автора - author и год выпуска - year. Полученные данные должны быть
#преобразованы в словарь book с ключами: title, author, year. Причем year
#нужно преобразовать в тип int.
title = input('Введите название книги: ')
author = input('Введите имя автора: ')
year = input('Введите год издания книги: ')
book = {'Название книги' : title, 'Автор' : author, 'Год' : int(year)}
print(book)