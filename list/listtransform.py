#1 Вывод из списка строки
new_list = ['one', 'two', 'tree']
print(', '.join(new_list))

#2 Вывод из списка столбцы
print('\n'.join(new_list))

#Первые два пункта не работают с элементами списка int
new_list_numbers = [21, 2331, 24, -56]

#Если вы просто хотите получить строку с разделителями-запятыми, вы можете использовать этот шаблон
print(str((new_list_numbers)).strip('[]'))      

#Вы можете использовать map() чтобы преобразовать каждый элемент в список строки и затем присоединиться к ним
print(', '.join(map(str, new_list_numbers)))    
print('\n'.join(map(str, new_list_numbers)))    