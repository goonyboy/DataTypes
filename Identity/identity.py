list_1 = ['a', 'b', 'c']
list_2 = list_1
list_3 = list(list_1)

print(list_1)
print(list_2)
print(list_3)

print(list_1 == list_2)     #True
print(list_1 == list_3)     #True

print(list_1 is list_2)     #True
print(list_1 is list_3)     #False

# Здесь мы можем увидеть (list_1 is list_3) False,
# потому что list_1 и list_3 указывают на два разных
# объекта, даже если их содержимое может быть одинаковым.
# Таким образом, мы можем сказать, что «is» вернёт True,
# если две переменные указывают на один и тот же объект,
# и «==», если объекты, на которые ссылаются переменные, равны.

# При работе со списками есть особенность, которую необходимо рассмотреть.

list = ['Hello', 'world']
new_list = list
print(new_list is list)     # True

new_list.append('!')
print(list)                 # ['Hello', 'world', '!']

# Чтобы избежать такого поворота событий, список нужно копировать.
new_list = list.copy()
print(new_list is list)     # False