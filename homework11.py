###############  ДЗ 11.1. Генератор простих чисел


# def prime_generator(end):
#     def is_prime(n):
#         if n <= 1:
#             return False
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     for num in range(2, end + 1):
#         if is_prime(num):
#             yield num
#
#
# print(list(prime_generator(10)))
# print(list(prime_generator(15)))
# print(list(prime_generator(29)))



###############  ДЗ 11.2. Заповнення списку кубами чисел

# def generate_cube_numbers(end):
#     n = 2
#     while True:
#         cube = n**3
#         if cube >= end:
#             return
#         yield cube
#         n += 1
#
# from inspect import isgenerator
#
# gen = generate_cube_numbers(1)
#
#
# assert isgenerator(gen) == True, 'Test0'
#
# print(list(generate_cube_numbers(10)))
# print(list(generate_cube_numbers(100)))
# print(list(generate_cube_numbers(1000)))





###############  ДЗ 11.1. Генератор простих чисел




# def is_even(number):
#     last_digit = str(number)[-1]
#     return last_digit in '02468'
#
#
# print(is_even(2494563894038**2))
# print(is_even(1056897**2))
# print(is_even(24945638940387**3))


