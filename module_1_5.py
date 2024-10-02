immutable_var = ([1,2 ],'tuple',True)   # Создание кортежа с разными типами данных: , list, str и bool.
print(immutable_var)                    # Вывод на печать созданного кортежа immutable_var.
#immutable_var[2] = False   т. к. элементы кортежа изменять нельзя, то данная строка при выполнении выдаст ошибку: "TypeError: 'tuple' object does not support item assignment", поэтому я ее закомментировал.
mmutable_list = [1,2,3,'apple'] # Создание списка, из четырех элементов.
mmutable_list[3] = 'pear'   # Замена 4-го элемента списка на другой.
print(mmutable_list)    # Вывод измененного элемента списка на печать.