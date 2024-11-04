####################  7.1


# def say_hi(name, age):
#   return f"Hi. My name is {name} and I'm {age} years old"
#
# print(say_hi("Alex", 32))
# print(say_hi("Frank", 68))
# assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
# assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
# print('ОК')


####################  7.2
#
# def correct_sentence(text):
#     sentences = text.split('. ')
#     corrected_sentences = []
#     for sentence in sentences:
#
#         sentence = sentence.strip()
#
#         if sentence:
#
#             sentence = sentence[0].upper() + sentence[1:]
#
#         if not sentence.endswith('.'):
#             sentence += '.'
#
#         corrected_sentences.append(sentence)
#
#     result = ' '.join(corrected_sentences)
#     print(result)
#     return result
#
#
# assert correct_sentence("greetings, friends")
# assert correct_sentence("hello")
# assert correct_sentence("Greetings, friends.")
# assert correct_sentence("Greetings, friends.")
# assert correct_sentence("greetings, friends.")
# print('ОК')

####################  7.3


# def second_index(text, some_str):
#     first_index = text.find(some_str)
#
#     if first_index == -1:
#         print(None)
#         return
#
#     second_index = text.find(some_str, first_index + len(some_str))
#
#     if second_index == -1:
#         print(None)
#     else:
#         print(second_index)
#
#
# second_index("sims", "s") == 3, 'Test1'
# second_index("find the river", "e") == 12, 'Test2'
# second_index("hi", "h") is None, 'Test3'
# second_index("Hello, hello", "lo") == 10, 'Test4'





####################  7.4


# def common_elements():
#
#     multi_3 = [x for x in range(100) if x % 3 == 0]
#     multi_5 = [x for x in range(100) if x % 5 == 0]
#
#     set_3 = set(multi_3)
#     set_5 = set(multi_5)
#
#     intersection = set_3.intersection(set_5)
#
#     print(intersection)
#
#
# common_elements()

