import re

"""
1) Дана довільна строка. Напишіть код, який знайде в ній і віведе на екран
кількість слів, які містять дві голосні літери підряд.
"""

task_lst = re.split(" ", input("Введіть рядок для перевірки: "))
vowels = "aeiouyауоыиэяюёеаоуеиі"
result_count = 0
for word in task_lst:
    word = filter(str.isalpha, word)
    word = "".join(word)
    if len(word) > 0:
        check_count = 0
        for i in range(len(word)):
            if word[i] in vowels:
                check_count += 1
            else:
                check_count = 0
            if check_count == 2:
                result_count += 1
                break
print(f"Кількість слів із двома голосними літерами - {result_count}")


