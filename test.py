import re
import random
import all_func

"""3) Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 'Lorem Ipsum']. 
Напишіть механізм, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1. 
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску."""
list_word = input("Введіть ваше речення: ")
list_word = re.split(" ", list_word)
result_list = []
for word in list_word:
    word = filter(str.isalpha, word)
    word = "".join(word)
    if len(word) > 0:
        result_list.append(word)
print(result_list)
