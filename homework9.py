#############   ДЗ 9.1. Визначити популярність певних слів у тексті

# def popular_words(text, words):
#
#     text = text.lower()
#
#     word_list = text.split()
#
#     word_count = {}
#
#     for word in words:
#         word_count[word] = word_list.count(word)  # Підраховуємо скільки разів слово з'являється
#
#     return word_count
#
# result = popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
# print(result)



#################   ДЗ 9.2. Різниця між числами

#
# def difference(*args):
#
#     if not args:
#         return 0
#
#
#     max_val = max(args)
#     min_val = min(args)
#
#     result = max_val - min_val
#
#     return round(result, 2)
#
#
# print(difference(1, 2, 3))
# print(difference(5, -5))
# print(difference(10.2, -2.2, 0, 1.1, 0.5))
# print(difference())
