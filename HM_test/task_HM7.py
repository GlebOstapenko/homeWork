from HM7.all_func_HM7 import get_int
from HM7.all_func_HM7 import check_palindrome


def get_user_age():
    """
    :return: Фукція повертає вік користувача у форматі int
    """
    while True:
        user_age = get_int("Вкажіть ваш вік: ")
        if user_age < 0:
            print("Як ти ростеш у мінус?) Вкажи, будь ласка, адекватний вік")
        else:
            return user_age


def get_age_form(age):
    """
    :param age: Приймає вік користувача
    :return: Повертає корректне значеня віку
    """
    check_age = str(age)[-1]
    if check_age == "1" and age != 11:
        return "рік"
    elif check_age in ["2", "3", "4"] and not (age in [12, 13, 14]):
        return "роки"
    else:
        return "років"


def hm7_task(age):
    """
    :param age: Вік користувача
    :return: Виводить відповідь магазину про можливість купівлі квитка
    """
    age_form = get_age_form(age)
    if age < 7:
        print(f"Тобі ж {age} {age_form}! Де твої батьки?")
    elif age < 16:
        if check_palindrome(age):
            print(f"{age} {age_form} - це чудовий вік, але це фільм для дорослих!")
        else:
            print(f"Тобі лише {age} {age_form}, а це фільм для дорослих!")
    elif age >= 65:
        if check_palindrome(age):
            print(f"{age} {age_form} - це чудовий вік, будь ласка, покажіть пенсійне посвідчення!")
        else:
            print(f"Вам {age} {age_form}? Покажіть пенсійне посвідчення!")
    else:
        if check_palindrome(age):
            print(f"{age} {age_form} - це чудовий вік, але треба було приходити раніше, квитків більше нема!")
        else:
            print(f"Незважаючи на те, що вам {age} {age_form}, білетів всеодно нема!")


if __name__ == '__main__':
    hm7_task(get_user_age())
