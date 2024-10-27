######## 5.1

import string
import keyword

test_data = ['_', '__', '___', 'x', 'get_value', 'get value', 'get!value', 'some_super_puper_value', 'Get_value',
             'get_Value', '3m', 'm3', 'assert', 'assert_exception']

for test_variable in test_data:
    if len(test_variable) > 0:
        if test_variable in keyword.kwlist:
            print(f"{test_variable} = False!")
        elif not test_variable[0].isnumeric() and test_variable.islower() and test_variable.count(" ") == 0:
            is_correct = True
            for symbol in string.punctuation.replace("_", " "):
                if symbol in test_variable:
                    is_correct = False
                    print(f"{test_variable} = False!")
                    break

            first_underscore_index = test_variable.find("_")
            if first_underscore_index >= 1:
                second_underscore_index = test_variable.find("_", first_underscore_index + 1)
                if second_underscore_index >= 1 and second_underscore_index + first_underscore_index == 2:
                    is_correct = False
                    print(f"{first_underscore_index} False! Found more 2 '_' !")

            if is_correct:
                        print(f"{test_variable} = True!")
        else:
              print(f"{test_variable} = False!")









######################## 5.2 ########################
#
# CONTINUE_PROGRAM = "y"
# while True:
#         print("Оберіть операцію.")
#         print("1. +")
#         print("2. -")
#         print("3. *")
#         print("4. /")
#         choice = input("Введіть число операції (1,2,3,4):")
#         num1 = float(input("Введіть перше число:"))
#         num2 = float(input("Введіть друге число:"))
#
#         if choice == "1":
#             print(num1, "+", num2,"=", num1+num2)
#         elif choice == "2":
#             print(num1, "-", num2,"=", num1-num2)
#         elif choice == "3":
#             print(num1, "*", num2, "=", num1*num2)
#         elif choice == "4":
#             print(num1, "/", num2, "=", num1/num2)
#         else:
#             print("Невірна операція!")
#         is_continue = input(f"Ви хочете продовжити програму? Натисніть букву \'{CONTINUE_PROGRAM}\' : ")
#
#         if is_continue != CONTINUE_PROGRAM:
#             print("Вихід з програми...")
#             break

################            5.3    ########################

# import string
# s = input("Введіть рядок:: ")
# s = s.title()
# s = s.replace(' ','')
# table = str.maketrans("", "", string.punctuation)
# new_s = s.translate(table)
# c = "#"
# n = 1
# s1 = c * n
# s2 = s1 + new_s
# if len(s1) > 140:
#     s1 = s1[:140]
#
# print(s2)

################################


