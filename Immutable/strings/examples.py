#1 
colors = 'yellow white green'                   #Создаем переменную colors 
print(colors.split())                           #С помощью split(разделитель - пробел) выводим список цветов 
colors_split = colors.split()                   #Записываем список цветов в переменную
colors_joined = ' and '.join(colors_split)      #Создаем новую переменную, в которой все данные из colors_split будут объединены через ' and '
print(colors_joined)                            #Выводим результат

#2
path = 'admin/downloads/telegram/web.html'      #Создаем переменную с путем файла
print(path.split('/'))                          #Выводим созданный список через разделитель '/'

#3
#Программа, которая каждое число из строки numbers, состоящую из чисел и пробелов, выводит построчно.
numbers = input()                               # Вводим числа
numbers_split = numbers.split()                 # Создаем список из введенных чисел
numbers_join = '\n'.join(numbers_split)         # Создаем переменную numbers_join, где разделитель - перенос на новую строку
print(numbers_join)                             # Выводим построчно содержимое переменной numbers_join

#4
#Выводим возраст пользователя
age = int(input())                                  #Ввод возраста
print('My age is ' + str(age) + ' years old!')      #Для вывода необходимо преобразовать переменную age из int в str\
print('wow ' * age)                                 #По одному 'wow' за прожитый год

#5
#Как должен выглядеть шаблон строки для вывода времени в записанном ниже формате?
# HH:MM:SS

hours = int(input())
minutes = int(input())
seconds = int(input())
print("%02d:%02d:%02d" % (hours, minutes, seconds))