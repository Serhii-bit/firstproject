##############  ДЗ 8.1. Додати 1 до числа
#
# def add_one(some_list):
#
#     num = 0
#     for digit in some_list:
#         num = num * 10 + digit
#
#     num += 1
#
#     result = [int(digit) for digit in str(num)]
#
#     print(result)
#     return result
#
#
# add_one([1, 2, 3, 4])
# add_one([9, 9, 9])
# add_one([0])
# add_one([9])

##############  ДЗ 8.2. Паліандром

# def is_palindrome(text):
#
#     clean_text = ''.join(c.lower() for c in text if c.isalnum())
#
#     result = clean_text == clean_text[::-1]
#
#     print(result)
#     return result
#
#
# is_palindrome('A man, a plan, a canal: Panama')
# is_palindrome('0P')
# is_palindrome('a.')
# is_palindrome('aurora')

##############  ДЗ 8.3. Унікальне число
#
# def find_unique_value(some_list):
#     for item in some_list:
#
#         if some_list.count(item) == 1:
#             print(item)
#             return item
#
#     print(None)
#     return None
#
#
#
# find_unique_value([1, 2, 1, 1])
# find_unique_value([2, 3, 3, 3, 5, 5])
# find_unique_value([5, 5, 5, 2, 2, 0.5])

