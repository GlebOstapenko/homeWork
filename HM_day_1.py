def get_num(word):
    while True:
        number = input(word)
        try:
            return (float(number))
        except:
            print("Ошибка, пробуй ещё раз ввести число")

# Задача 1: Створіть дві змінні first=10, second=30.
# Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
first_number = get_num("Укажите первое число: ")
second_number = get_num("Укажите второе число: ")
print("Задача 1")
print(f"{first_number} + {second_number} = {first_number + second_number}")
print(f"{first_number} - {second_number} = {first_number - second_number}")
print(f"{first_number} * {second_number} = {first_number * second_number}")
print(f"{first_number} / {second_number} = {first_number / second_number}")
print(f"{first_number} ** {second_number} = {first_number ** second_number}")
print(f"{first_number} // {second_number} = {first_number // second_number}")
print(f"{first_number} % {second_number} = {first_number % second_number}")

# Задача 2: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1.
# Виведіть на екран результат кожного порівняння.
print("\nЗадача 2")
task_number = first_number > second_number
print(f"{first_number} > {second_number} - {task_number}")
task_number = first_number < second_number
print(f"{first_number} < {second_number} - {task_number}")
task_number = first_number == second_number
print(f"{first_number} == {second_number} - {task_number}")
task_number = first_number != second_number
print(f"{first_number} != {second_number} - {task_number}")

# Задача 3: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world".
# Виведіть на екран.
print("\nЗадача 3")
count_word = int(input("Укажите количество слов в предложении: "))
sentence = ""
for i in range(1, count_word + 1):
    word = input(f"Введите слово №{i}: ")
    sentence = sentence + word + " "
print(sentence)
