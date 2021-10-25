# Вывод в консоль всех ключевых слов
import keyword

print('\n','Список ключевых слова в Python: ', keyword.kwlist,'\n')

# Создение переменных всех типов
string1 = "Переменная типа строка"            # Строка
int1 = 23                                     # Целочисленный
float1 = 2.71                                 # С плавающей точкой
b = bytes(23)                                 # Байты
list1 = list('Roman')                         # Список
tuple1 = ('Imagine', 'all', 'the', 'people')  # Кортеж
set1 = set('hello worllld')                   # Множество, изменяемый неупорядоченный тип данных. В множестве всегда содержатся
                                              # только уникальные элементы.
frozenset1 = frozenset('trololoev')           # Множество, НЕизменяемый неупорядоченный тип данных
dict1 = {                                     # Словарь, изменяемый упорядоченный тип данных, доступ к значениям осуществляется по ключу dict1['name']
    'name': 'Roman',
    'Head': 1,
    'brain': 1,
    'percentage of brain use': 1,
    'hands': 2,
    'legs': 2,
    'dream': 'Become a QA hokage'
}
# Вывод в консоль всех переменных и их типов
print(string1, type(string1), '\n', int1, type(int1), '\n', float1, type(float1), '\n', b, type(b), '\n', list1,
      type(list1), '\n', tuple1, type(tuple1), '\n', set1, type(set1), '\n', frozenset1, type(frozenset1), '\n', dict1,
      type(dict1), '\n', )

# Конкатенация строк
str1 = 'apple '
str2 = 'pen'
str3 = str1 + str2
print(str3)

# Вывод в одну строку переменных типа String и Integer используя “,”
print(str3, int1)

# Вывод в одну строку переменных типа String и Integer используя “+” (Плюс)
print(str3 + ' ' + str(int1))
