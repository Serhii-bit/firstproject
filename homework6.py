#################  ДЗ 6.1. Діапазон букв

# import string
#
# ALL_LETTERS = string.ascii_letters
# SEPARATOR = "-"
#
# user_input = input("Введіть букви як в прикладі: 'a-c' ").strip()
#
# if len(user_input) == 3:
#     first_letter = user_input[0]
#     second_letter = user_input[2]
#     separator = user_input[1]
#
#     if first_letter.isalpha() and second_letter.isalpha() and separator == SEPARATOR:
#         start_index = ALL_LETTERS.index(first_letter)
#         end_index = ALL_LETTERS.index(second_letter)
#
#         if start_index > end_index:
#             start_index, end_index = end_index, start_index
#
#         result = ALL_LETTERS[start_index:end_index + 1]
#         print(result)





#################  ДЗ 6.2. Конвертер із числа в дату


# t = int(input("Введіть кількість секунд!:"))
# days = t // (24*60*60)
# hours = (t % (24*60*60)) // (60*60)
# minutes = (t % (60*60)) // 60
# seconds = t % 60
# print(f"{days}дні, {hours}:{minutes}:{seconds}")



#################  ДЗ 6.3. Добуток чисел



# t = int(input("Введіть суму!:"))
#
# while t > 9:
#     temp_t = str(t)
#     t = 1
#     for char in temp_t:
#         if char.isdigit():
#             t *= int(char)
#     print(t)