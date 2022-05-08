import sqlite3 as sql
from game_func import get_choice, get_computer_choice, check_winner
from all_func import get_any_type
from text import main_menu, res_menu


def add_game_result(user_choice, computer_choice, result):
    """
     Додає новий запис до БД
     :param user_choice: хід користувача
     :param computer_choice: хід комп'ютера
     :param result: результат гри
     """
    new_result_info = (user_choice, computer_choice, result)
    cur.execute(f"INSERT INTO games_results VALUES(?, ?, ?)", new_result_info)


def my_game():
    """
    Гра - Камінь, ножиці, папір, ящірка, спок
    """
    user_choice = get_choice("user")
    computer_choice = get_computer_choice()
    result = check_winner(user_choice, computer_choice)
    add_game_result(user_choice, computer_choice, result)


def output_db_info(func):
    """
    Декоратор який виводить в консоль результат функцій, які в свою чергу дістають з БД інформацію
    за певними фільтрами P.S. фільтри дивитись у функціях
    """

    def output(type_results):
        results = func(type_results)
        print("=" * 36)
        if len(results) == 0:
            print("Нет информации по данному запросу")
        else:
            print("User choice Computer choice Winner")
            for result in results:
                user_choice = result[0] + (" " * (11 - len(result[0])))
                computer_choice = result[1] + (" " * (15 - len(result[1])))
                winner = result[2]
                print(user_choice, computer_choice, winner)
        print("=" * 36)

    return output


@output_db_info
def get_results_list(type_results):
    """
    :param type_results: "all" показую весь список, будь яка інша інформация фільтрується у колонці winner
    :return: повертає відфільтровану інформацію
    """

    if type_results == "all":
        cur.execute("SELECT * FROM games_results ")
        results = cur.fetchall()
        return results
    else:
        cur.execute(f"SELECT * FROM games_results WHERE winner == '{type_results}' ")
        results = cur.fetchall()
        return results


@output_db_info
def get_results_for_choice(who_choice):
    """
    :param who_choice: введена інформація+_choice відповідаю назві колонки в якій шукаємо
    :return: повертає список ігор у яких комп'ютер або гравець вибирали певний хід
    """
    search_choice = get_choice("search")
    cur.execute(f"SELECT * FROM games_results WHERE {who_choice}_choice == '{search_choice}'")
    results = cur.fetchall()
    return results


if __name__ == '__main__':
    with sql.connect("game.sqlite3") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS games_results (
        user_choice TEXT,
        computer_choice TEXT,
        winner  TEXT
        )""")
    while True:
        print(main_menu)
        act_application = get_any_type("Введіть дію: ", "str_only_words")
        if act_application == "game":
            my_game()
        elif act_application == "res":
            print(res_menu)
            act_application = get_any_type("Введіть дію: ", "str_only_words")
            if act_application == "all":
                get_results_list(act_application)
            elif act_application == "win":
                act_application = get_any_type("Виберіть 'user' або 'computer': ", "str_only_words")
                get_results_list(act_application)
            elif act_application == "cho":
                act_application = get_any_type("Виберіть чий хід 'user' або 'computer': ", "str_only_words")
                get_results_for_choice(act_application)
        else:
            break
