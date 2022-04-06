#Задача 1: Створіть дві змінні first=10, second=30.
#Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
first_number = int(input(f"Укажите первое число: "))
second_number = int(input(f"Укажите второе число: "))

print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")
print(f"{first_number} ** {second_number} = {first_number ** second_number}")
print(f"{first_number} // {second_number} = {first_number // second_number}")
print(f"{first_number} % {second_number} = {first_number % second_number}")

#Задача 2: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
#Виведіть на екран результат кожного порівняння.
task_number = first_number > second_number
print(f"{first_number} > {second_number} - {task_number}")
task_number = first_number < second_number
print(f"{first_number} < {second_number} - {task_number}")
task_number = first_number == second_number
print(f"{first_number} == {second_number} - {task_number}")
task_number = first_number != second_number
print(f"{first_number} != {second_number} - {task_number}")

#Задача 3: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
#Виведіть на екран.
count_word = int(input("Укажите количество слов в предложении: "))
sentence = ""
for i in range(count_word):
    word = input(f"Введите слово №{i + 1}: ")
    sentence = sentence + word + " "
    i = i + 1
print(sentence)