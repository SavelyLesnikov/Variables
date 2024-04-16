immutable_var = (318, 'Спасибо', True)
print(immutable_var)
#immutable_var[1] = 'Пожалуйста' - Ошибка, так как элементы кортежа неизменяемы, если предварительно их не добавить в список внутри кортежа.
immutable_var = (318, ['Спасибо'], True)
immutable_var[1][0] = 'Пожалуйста'
print(immutable_var)
#Таким образом - можно менять значения изменяемых элементов кортежа.
mutable_list = [False, 'Привет', 512]
print(mutable_list)
mutable_list[0] = True
mutable_list[1] = 'Пока'
mutable_list[2] = 1024
mutable_list.append('Modified')
mutable_list.extend([440, False])
print(mutable_list)
