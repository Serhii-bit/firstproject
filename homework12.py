
################  ДЗ 12.1. Очистити текст від html-тегів

# import re
#
#
# def delete_html_tags(html_file, result_file='cleaned.txt'):
#
#     try:
#         with open(html_file, 'r', encoding='utf-8') as file:
#             html_content = file.read()
#     except FileNotFoundError:
#         print(f"Файл {html_file} не знайдено!")
#         return
#
#     cleaned_content = re.sub(r'<.*?>', '', html_content)
#
#     cleaned_content = '\n'.join(line.strip() for line in cleaned_content.splitlines() if line.strip())
#
#     with open(result_file, 'w', encoding='utf-8') as file:
#         file.write(cleaned_content)
#
#     print(f"HTML теги були видалені, і текст збережений в файл: {result_file}")
#
#
#
# # delete_html_tags('draft.html')

################  ДЗ 12.2. Корзина для покупок

# class Item:
#
#     def __init__(self, name, price, description, dimensions):
#         self.price = price
#         self.description = description
#         self.dimensions = dimensions
#         self.name = name
#
#     def __str__(self): # lemon, price: 5
#         # print(self.dimensions)
#         return f"{self.name}, price: {self.price}"
#
#
# class User:
#
#     def __init__(self, name, surname, numberphone):
#         self.name = name
#         self.surname = surname
#         self.numberphone = numberphone
#
#     def __str__(self):
#         return f"{self.name.title()} {self.surname.title()}"
#
#
# class Purchase:
#     def __init__(self, user):
#         self.products = {}
#         self.user = user
#         self.total = 0
#
#     def add_item(self, item, cnt):
#         self.products[item] = cnt
#
#     def __str__(self):
#         all_products = ""
#         for product, count in self.products.items():
#             all_products += f"\n{product.name}: {count} pcs."
#         return f"User: {self.user}\nItems:{all_products}"
#
#     # """
#     # User: Ivan Ivanov
#     # Items:
#     # lemon: 4 pcs.
#     # apple: 20 pcs.
#     # """
#
#     def get_total(self):
#         all_sum = 0
#         for product, count in self.products.items():
#             all_sum += (product.price * count)
#         return all_sum
#
#
# lemon = Item('lemon', 5, "yellow", "small")
# print(lemon)
# # test1 = lemon.__str__()
# # print(test1)
# # test2 = str(lemon)
# # print(test2)
# apple = Item('apple', 2, "red", "middle")
# # print(lemon)  # lemon, price: 5
# buyer = User("Ivan", "Ivanov", "02628162")
# print(buyer)  # Ivan Ivanov
# #
# cart = Purchase(buyer)
# cart.add_item(lemon, 4)
# cart.add_item(apple, 20)
# print(cart)
# print(cart.get_total())
# # """
# # User: Ivan Ivanov
# # Items:
# # lemon: 4 pcs.
# # apple: 20 pcs.
# # """
# assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
# assert cart.get_total() == 60, "Всього 60"
# assert cart.get_total() == 60, 'Повинно залишатися 60!'
# cart.add_item(apple, 10)
# print(cart)
# # """
# # User: Ivan Ivanov
# # Items:
# # lemon: 4 pcs.
# # apple: 10 pcs.
# # """
# #
# assert cart.get_total() == 40

