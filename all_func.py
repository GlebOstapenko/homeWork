# Получение переменной опраделённого типа
def get_any_type(word, search_type):
    if search_type == "float":
        while True:
            my_number = input(word)
            try:
                return float(my_number)
            except:
                print("Ошибка, пробуй ещё раз ввести число")

    elif search_type == "int":
        while True:
            my_number = input(word)
            try:
                return int(my_number)
            except:
                print("Ошибка, пробуй ещё раз ввести число")

    elif search_type == "str_only_words":
        while True:
            my_str = input(word)
            if my_str.isalpha() and not " " in my_str:
                return my_str
            else:
                print("Ошибка, пробуй ещё раз ввести данные (слово без цифр, символов или пробелов)")


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


# Удаление пунка в словаре
def delete_tile_list(delete_tile, correct_list):
    result_list = {}
    if delete_tile in correct_list:
        for tile in correct_list:
            if delete_tile != tile:
                result_list.update({tile: correct_list[tile]})
        return result_list
    else:
        print("Нет такого фильма в списке")


# Выведение словаря в виде списка (available_information - допустимая информация для отображения)
def check_list(checking, available_information):
    print("=========================")
    for keys in checking:
        print(keys)
        for i in range(available_information):
            print(checking[keys][i])
        print("=========================")
