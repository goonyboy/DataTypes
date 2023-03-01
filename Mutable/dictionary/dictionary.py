#1 Создание словаря
person = {'name' : 'Alex Gold'}                  #Создадим словарь пользователя
print(person)                               #{'name': 'Alex Gold'}
person['age'] = 20                          #Добавим несколько новых элементов словаря
person['email'] = 'alexgold@example.com'
person['phone'] = '+7(921)-272-27-27'
print(person)       #{'name': 'Alex Gold', 'age': 20, 'email': 'alexgold@example.com', 'phone': '+7(921)-272-27-27'}
print(person.keys())                        #Выводим список всех ключей
print(person.values())                      #Выводим список всех значений

person.pop('phone')                         #Удаляем значение phone
print(person)                               #{'name': 'Alex Gold', 'age': 20, 'email': 'alexgold@example.com'}

