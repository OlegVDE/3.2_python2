# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/116BaY_eNUhvukXNTUBZtV3oyWPWL4d2y
"""

# Напишите функцию, которая будет принимать на вход длину стороны квадрата и выводить на экран площадь квадрата и его периметр.
def square(a):
  print(f'Площадь квадрата со стороной {a} равна {a*a}')
  print(f'Периметр квадрата со стороной {a}  равен {a*4}')

square(5)

# Напишите функцию, которая будет принимать два числа и считать сумму квадратов этих двух чисел, запишите своё вычисление в переменную squared.
def square2(a, b):
  return a * a + b * b

squared = square2(4,5)
squared

# Напишите функцию, которая будет принимать на вход список [“male“,“male“,“female“,“male“,“male“,“female“,”female“] и возвращать его в обратном порядке. Запишите список в переменную new_list.
def list_mirror(spisok):
  return spisok[::-1]

ans = list_mirror(["male","male","female","male","male","female","female"])
ans

# Напишите функцию, которая будет принимать на вход список из предыдущего задания(new_list) и выводить на экран количество мужчин или количество женщин в зависимости от требований пользователя.
# Подсказка: вам необходимо добавить еще один параметр в описание функции
def count_sex(my_list, sex):
  print(my_list.count(sex))

my_list = ["male","male","female","male","male","female","female"]
sex = "male"
count_sex(my_list, sex)

# Напишите функцию, которая будет принимать строку (Например: “female”), а возвращать словарь где ключи — это символы строки, а значения кол-во символов в строке.
def count_char(string):
  result = {}
  for char in string:
    result[char] = string.count(char)
  return result

string = "female"
result = count_char(string)
print("Результат: ", result)







