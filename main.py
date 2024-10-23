################# 4.1

# arr = [0, 1, 0, 12, 3]
# def move_zeros_to_right(arr):
#     count_zeros = 0
#     for num in arr:
#         if num == 0:
#             count_zeros += 1
#     result = [num for num in arr if num !=0] + [0] * count_zeros
#     return result
# new_arr = move_zeros_to_right(arr)
# print(new_arr)
#################

# arr = [0]
# def move_zeros_to_right(arr):
#     count_zeros = 0
#     for num in arr:
#         if num == 0:
#             count_zeros += 0
#             return result
# print(arr)

#################

# arr = [1, 0, 13, 0, 0, 0, 5]
# def move_zeros_to_right(arr):
#     count_zeros = 0
#     for num in arr:
#         if num == 0:
#             count_zeros += 1
#     result = [num for num in arr if num !=0] + [0] * count_zeros
#     return result
# new_arr = move_zeros_to_right(arr)
# print(new_arr)

###################

# arr = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
# def move_zeros_to_right(arr):
#     count_zeros = 0
#     for num in arr:
#         if num == 0:
#             count_zeros += 1
#     result = [num for num in arr if num !=0] + [0] * count_zeros
#     return result
#
# new_arr = move_zeros_to_right(arr)
# print(new_arr)

############### ###### ДЗ 4.2

# numbers = [1, 3, 5]
# if len(numbers) != 0:
#     summa = 0
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             summa += numbers[i]
#     result = summa * numbers[-1]
# else:
#     result = 0
# print(f"Result: {result}")
#


# numbers = [6]
# if len(numbers) != 0:
#     summa = 0
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             summa += numbers[i]
#     result = summa * numbers[-1]
# else:
#     result = 0
# print(f"Result: {result}")



# numbers = []
# if len(numbers) != 0:
#     summa = 0
#     for i in range(len(numbers)):
#         if i % 2 == 0:
#             summa += numbers[i]
#     result = summa * numbers[-1]
# else:
#     result = 0
# print(f"Result: {result}")



################## ДЗ 4.3



# import random
# numbers = []
# for i in range(random.randint(3, 10)):
#     numbers.append(random.randint(3, 10))
# print("random numbers")
# print(numbers)
# print("Числа по індексу (0, 2, -2)")
# numbers = [numbers[0], numbers[2], numbers[-2]]
# print(numbers)






