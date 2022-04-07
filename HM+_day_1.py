def get_num_float(word):
    while True:
        number = input(word)
        try:
            return (float(number))
        except:
            print("Ошибка, пробуй ещё раз ввести число")

def get_num_int(word):
    while True:
        number = input(word)
        try:
            return (int(number))
        except:
            print("Ошибка, пробуй ещё раз ввести число")

trigger = "start"
while trigger == "start":
    print("""
Домашня робота
Задача 1: Створіть дві змінні first=10, second=30. 
Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.) для цих чисел.
Задача 2: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=) чисел з завдання 1. 
Виведіть на екран результат кожного порівняння.
Задача 3: Створіть змінну - результат конкатенації (складання) строк str1="Hello " и str2="world". 
Виведіть на екран.\n""")
    task_number = 0
    while task_number != "1" and task_number != "2" and task_number != "3":
        task_number = str(input("Введите номер задания: "))
        if task_number != "1" and task_number != "2" and task_number != "3":
            print("Вы указани не правильный номер задания, попробуйте ещё раз!")

    if task_number == "1" or task_number == "2":
        print(f"Введите, пожалуйста, числа для задания №{task_number} "
              "(пожалуйста, укажите числа, так как не смог реализовать контроль типа данных)")
        first_number = get_num_float("Укажите первое число: ")
        second_number = get_num_float("Укажите второе число: ")

    # First task
    if task_number == "1":
        print("\nЗадача 1 ")
        task_number = str(input("""Список доступных действий:
"+" - Сложение
"-" - Вычитание
"*" - Умножение
"/" - Деление
"**" - Возведение в степень
"//" - Целочисленное деление
"%" - Деление по модулю
Любой другой символ, цифра или буква, покажет все действия.
Укажите, пожалуйста, нелбходимое дейтсвие: """))
        if task_number == "+":
            print(f"{first_number} + {second_number} = {first_number + second_number}")
        elif task_number == "-":
            print(f"{first_number} - {second_number} = {first_number - second_number}")
        elif task_number == "*":
            print(f"{first_number} * {second_number} = {first_number * second_number}")
        elif task_number == "/":
            print(f"{first_number} / {second_number} = {first_number / second_number}")
        elif task_number == "**":
            print(f"{first_number} ** {second_number} = {first_number ** second_number}")
        elif task_number == "//":
            print(f"{first_number} // {second_number} = {first_number // second_number}")
        elif task_number == "%":
            print(f"{first_number} % {second_number} = {first_number % second_number}")
        else:
            print(f"{first_number} + {second_number} = {first_number + second_number}")
            print(f"{first_number} - {second_number} = {first_number - second_number}")
            print(f"{first_number} * {second_number} = {first_number * second_number}")
            print(f"{first_number} / {second_number} = {first_number / second_number}")
            print(f"{first_number} ** {second_number} = {first_number ** second_number}")
            print(f"{first_number} // {second_number} = {first_number // second_number}")
            print(f"{first_number} % {second_number} = {first_number % second_number}")

    # Second task
    elif task_number == "2":
        print("\nЗадача 2")
        task_number = first_number > second_number
        print(f"{first_number} > {second_number} - {task_number}")
        task_number = first_number < second_number
        print(f"{first_number} < {second_number} - {task_number}")
        task_number = first_number == second_number
        print(f"{first_number} == {second_number} - {task_number}")
        task_number = first_number != second_number
        print(f"{first_number} != {second_number} - {task_number}")

    #Third task
    else:
        print("\nЗадача 3")
        count_word = get_num_int("Укажите количество слов в предложении: ")
        sentence =""
        for i in range(1, count_word + 1):
            word = input(f"Введите слово №{i}: ")
            sentence = sentence + word + " "
        print(sentence)

    while task_number != "continue" and task_number != "end":
        task_number = str(input("Введите 'continue' что-бы продолжить проверку, или 'end' что-бы завершить: "))
        if task_number != "continue" and task_number != "end":
            print("Ви вказали неправильну команду, спробуйте ще!")
        elif task_number == "end":
            trigger = "start1"
            print("Спасибо за проверку)")



