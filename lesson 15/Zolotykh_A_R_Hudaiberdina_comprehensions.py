# Задание № 1
first_list = [1,2,3]
second_list = [10,20,30]
result_list = [(i,j) for i in first_list for j in second_list]
print(result_list)

# Задание № 2
# вариант выволнения с использованием функции
def is_palindrome(list_element:str):
    return list_element == list_element[::-1]
word_list = ['радар', 'мадам', 'утро', 'казак', 'топот', 'стул']
dictionary = {}
[dictionary.update({i:is_palindrome(i)}) for i in word_list]
print(dictionary)
# # вариант выполнения без использования функции
word_list = ['радар', 'мадам', 'утро', 'казак', 'топот', 'стул']
[dictionary.update({i:(i==i[::-1])}) for i in word_list]
print(dictionary)

# Задание № 3
words = ['apple', 'banana', 'orange', 'avocado', 'lime', 'artichoke']
vowels = 'aeiou'
result_list = [i for i in words if i.lower()[0] in vowels]
[print(i) for i in result_list]

#Задание № 4
unique_symbol_list = []
words = ['hello', 'world', 'python', 'programming']
[unique_symbol_list.append(j) for i in words for j in i if j not in unique_symbol_list]
print(sorted(unique_symbol_list))
