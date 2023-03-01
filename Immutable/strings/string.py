# Программа, которая каждое число из строки numbers, состоящую из чисел и пробелов, выводит построчно.

numbers = input('Введите числа через пробел: ')     # Вводим числа
numbers_split = numbers.split()                     # Создаем список из введенных чисел
print(numbers_split)                                # Выводим список на экран, проверив создался ли он корректно
numbers_stroke = '\n'.join(numbers_split)
print(numbers_stroke)

# Теперь из списка numbers_split нам необходимо вывести числа построчно


