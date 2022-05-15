from all_func import get_any_type
from random import choice
from text import choice_list, rules


def check_correct_choice(func):
    """
     Декоратор для функції, який перевіряє хід, який ввів користувач на коректність та відповідність до списку доступних
     Якщо користувач ввів не правильну інформацію, буде проведена повторна спроба введення
    """
    def check_choice(*args):
        while True:
            if (result := func(*args)) in choice_list:
                return result
            else:
                print("Немає такого ходу в цій грі спробуй ще: ")

    return check_choice


@check_correct_choice
def get_choice(get_type):
    """

    :param get_type: Приймає значення для фільтра, який визначає текс повідомлення під час введення
    :return: Повертає обраний хід зі списку у нижньому регістрі
    """
    if get_type == "user":
        user_choice = get_any_type(f"Введіть свій хід для гри {choice_list}: ", "str_only_words")
        return user_choice.lower()
    elif get_type == "search":
        print(f"Доступні фільтри для пошуку по ходу {choice_list}")
        search_choice = get_any_type(f"Введіть по якому ходу робитимемо вибірку: ", "str_only_words")
        return search_choice.lower()


def get_computer_choice():
    """
    :return: Повертає випадковий хід зі списку для комп'ютера у форматі str
    """
    computer_choice = choice(choice_list)
    print(f"Комп'ютер вибрав - {computer_choice}")
    return computer_choice


def check_winner(user_choice, computer_choice):
    """
    :param user_choice: хід користувача
    :param computer_choice: хід комп'ютера
    :return: повертає результати гри
    """
    if user_choice == computer_choice:
        print("Draw")
        return "draw"
    elif computer_choice in rules[user_choice]:
        print("User win!!!")
        return "user"
    else:
        print("Computer Win!!!")
        return "computer"