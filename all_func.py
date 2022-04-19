import random
import string
from rich.console import Console
from rich.console import Style

console = Console()
error_style = Style(color="red")


# Получение переменной опраделённого типа
def get_any_type(word, search_type):
    if search_type == "float":
        while True:
            my_number = console.input(word)
            try:
                return float(my_number)
            except:
                console.print("Помилка, спробуй ще раз ввести число", style=error_style)

    elif search_type == "int":
        while True:
            my_number = console.input(word)
            try:
                return int(my_number)
            except:
                console.print("Помилка, спробуй ще раз ввести число", style=error_style)

    elif search_type == "str_only_words":
        while True:
            my_str = console.input(word)
            if my_str.isalpha() and not " " in my_str:
                return my_str
            else:
                console.print("Помилка, спробуй ще раз ввести дані (слово без цифр, символів або пробілів)",
                              style=error_style)



# Проверка числа на палиндром
def check_palindrome(num):
    num = str(num)
    left_bord = ""
    right_bord = ""
    centre = ""
    if int(num) < 10:
        return False
    elif len(num) % 2 == 0:
        for i in range(len(num)):
            if i < len(num) / 2:
                left_bord += num[i]
            else:
                right_bord += num[i]
        return left_bord == right_bord
    else:
        for i in range(len(num)):
            if i < (len(num) / 2) - 1:
                left_bord += num[i]
            elif i > (len(num) / 2):
                right_bord += num[i]
            else:
                centre += num[i]
        return left_bord == right_bord


# Проверка входит ли слово в определённый список
def check_one_in_list(word, list_word):
    for i in list_word:
        if i == word:
            return True
    return False


# Проверка входит ли слово в определённый список 2.0
def new_check_one_in_list(word, list_word, error_message):
    while True:
        check_word = console.input(word).lower()
        if check_one_in_list(check_word, list_word):
            return check_word
        else:
            console.print(error_message)


# Логин пользователя (ключ словаря - логин, первый пункт списка - пароль)
def check_user_login(user_list):
    while True:
        user_login = str(input("Введите ваш логин: "))
        if user_login == "registry":
            return user_login
        user_password = str(input("Введите ваш пароль: "))
        try:
            if user_list[user_login][0] == user_password:
                return user_login
            else:
                print("Не верный пароль, попробуй ещё")

        except:
            print("Не верный логин, попробуй ещё или введи в поле логина (registry) для регистрации")


# Выведение словаря в виде списка (available_information - допустимая информация для отображения)
def check_dict(checking, available_information):
    print("=========================")
    for keys in checking:
        print(keys)
        for i in range(available_information):
            print(checking[keys][i])
        print("=========================")


# Создание списка (create_type - тип создания списка "full_rand","type_rand","value_rand","manual")
def create_list(create_type):
    while True:
        length = get_any_type("[blue]Введіть необхідний [yellow]розмір для списку[/yellow]: [/blue]", "int")
        if length>0:
            break
        else:
            console.print("[red]Введите число больше 0!!![/red]")
    result_list = []
    for i in range(length):
        if create_type == "type_rand" or create_type == "full_rand":
            variable_type = random.choice(["int", "str", "float", "bool"])
        else:
            variable_type = new_check_one_in_list("""[blue]Доступні типи 
[yellow]int[/yellow] - ціле число
[yellow]str[/yellow] - слово, речення або будь які символы
[yellow]float[/yellow] - число з цифрою після крапки
[yellow]bool[/yellow] - логічний тип данных.
Вкажіть тип змінної: [/blue]""", ["int", "str", "float", "bool"], "[red]Вказано не вірний тип, спробуй ще[/]")

        if variable_type == "int":
            if create_type == "value_rand" or create_type == "full_rand":
                result_list.append(random.randint(0, 100))
            else:
                result_list.append(get_any_type("[blue]Введіть [yellow]ціле число[/yellow]: [/blue]", "int"))

        elif variable_type == "str":
            if create_type == "value_rand" or create_type == "full_rand":
                letters = string.ascii_lowercase
                rand_length = random.randint(0, 10)
                word = ""
                for i in range(rand_length):
                    word += random.choice(letters)
                result_list.append(word)
            else:
                result_list.append(console.input("[blue]Введіть [yellow]значення[/yellow] для строки: [/blue]"))

        elif variable_type == "float":
            if create_type == "value_rand" or create_type == "full_rand":
                result_list.append(random.uniform(0, 10))
            else:
                result_list.append(get_any_type("[blue]Введіть [yellow]буль яке число[/yellow] (float): [/blue]",
                                                "float"))

        elif variable_type == "bool":
            if create_type == "value_rand" or create_type == "full_rand":
                result_list.append(bool(random.randint(0, 1)))
            else:
                result_list.append(
                    bool(console.input(
                        "[blue]Введіть [yellow]будь-яке значення[/yellow] для True, "
                        "просто натисніть [yellow]'Enter'[/yellow] для False: [/blue]")))
    return result_list


# Создание из одного списка, списка с определённым типом данных
def list_one_type(list_type, check_list):
    if list_type == "int":
        list_type = int
    elif list_type == "str":
        list_type = str
    elif list_type == "float":
        list_type = float
    elif list_type == "bool":
        list_type = bool
    result_list = []
    for tile in check_list:
        if type(tile) == list_type:
            result_list.append(tile)
    return result_list


# Список на экран в формате (Данные - тип данных)
def print_list_and_type(check_list):
    if len(check_list)==0:
        console.print("[red]Список порожній[/]")
    else:
        for tile in check_list:
            result_type = str(type(tile))
            console.print(f"[blue]{tile}[green] - тип ячейки [/green]{result_type[8:-2]}[/blue]")
