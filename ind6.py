#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Используя замыкания функций, объявите внутреннюю функцию, которая принимает два
параметра a , b , а затем, возвращает строку в формате: «Для значений a, b функция f(a,b) =
<число>» где число – это вычисленное значение функции f . Ссылка на f передается как
аргумент внешней функции. Вызовите внутреннюю функцию замыкания и отобразите на
экране результат ее работы. Функцию f придумайте самостоятельно (она должна что то
делать с двумя параметрами a , b и возвращать результат).
"""


def fun1():
    def fun2(a, b):
        return a + b
    return fun2


if __name__ == '__main__':
    a = int(input("введите а "))
    b = int(input("введите b "))
    test_fun = fun1()
    print("Для значений a, b функция f'(a,b) =", test_fun(a, b))
