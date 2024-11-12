#########   ДЗ 10.1. Генераторна функція
#
# def pow(x):
#     return x ** 2
#
# def some_gen(begin, end, func):
#     """
#     begin: перший елемент послідовності
#     end: кількість елементів у послідовності
#     func: функція, яка формує значення для послідовності
#     """
#     current = begin
#     for _ in range(end):
#         yield current
#         current = func(current)
#
# from inspect import isgenerator
#
# gen = some_gen(2, 4, pow)
#
# assert isgenerator(gen) == True, 'Test1'
# assert list(gen) == [2, 4, 16, 256], 'Test2'
#
# print('OK')



##########   ДЗ 10.2. Знайти перше слово
#


# import re
#
# def first_word(text):
#     """Знайти перше слово в рядку."""
#     match = re.search(r"[a-zA-Z0-9']+", text.strip())
#     if match:
#         return match.group(0)
#     return ""
#
#
# print(first_word("Hello world"))
# print(first_word("greetings, friends"))
# print(first_word("don't touch it"))
# print(first_word(".., and so on ..."))
# print(first_word("hi"))
# print(first_word("Hello.World"))









############   ДЗ 10.3. Перевірити чи є парним чи ні



# def is_even(digit):
#     """ Перевірка чи є парним число """
#     return digit % 2 == 0
#
#
# assert is_even(2) == True, 'Test1'
# assert is_even(5) == False, 'Test2'
# assert is_even(0) == True, 'Test3'
# print('OK')
