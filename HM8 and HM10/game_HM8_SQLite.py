import sqlite3 as sql
from game_func import get_choice, get_computer_choice, check_winner
from all_func import get_any_type, check_one_in_list
from text import main_menu, res_menu
from datetime import datetime
from func_get_file import get_results_file


def add_game_result(user_choice, computer_choice, result):
    """
     Додає новий запис до БД
     :param user_choice: хід користувача
     :param computer_choice: хід комп'ютера
     :param result: результат гри
     """
    new_result_info = (user_choice, computer_choice, result, datetime.now())
    cur.execute(f"INSERT INTO games_results VALUES(?, ?, ?, ?)", new_result_info)
    print("----------")
    con.commit()


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
            print("Game number User choice Computer choice Winner    Game datetime")
            for result in results:
                game_number = str(result[0]) + (" " * (11 - len(str(result[0]))))
                user_choice = result[1] + (" " * (11 - len(result[1])))
                computer_choice = result[2] + (" " * (15 - len(result[2])))
                winner = result[3] + (" " * (9 - len(result[3])))
                game_datetime = result[4]
                print(game_number, user_choice, computer_choice, winner, game_datetime)
        print("=" * 70)
        return results

    return output


@output_db_info
def get_results_list(type_results):
    """
    :param type_results: "all" показую весь список, будь яка інша інформация фільтрується у колонці winner
    :return: повертає відфільтровану інформацію
    """

    if type_results == "all":
        cur.execute("SELECT rowid, * FROM games_results ")
        results = cur.fetchall()
        print(type(results))
        return results
    else:
        cur.execute(f"SELECT rowid, * FROM games_results WHERE winner == '{type_results}' ")
        results = cur.fetchall()
        return results


@output_db_info
def get_results_for_choice(who_choice):
    """
    :param who_choice: введена інформація+_choice відповідаю назві колонки в якій шукаємо
    :return: повертає список ігор у яких комп'ютер або гравець вибирали певний хід
    """
    search_choice = get_choice("search")
    cur.execute(f"SELECT rowid, * FROM games_results WHERE {who_choice}_choice == '{search_choice}'")
    results = cur.fetchall()
    return results


if __name__ == '__main__':
    with sql.connect("game.sqlite3") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS games_results (
        user_choice TEXT,
        computer_choice TEXT,
        winner  TEXT
        game_datetime TEXT
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
                result_list = get_results_list(act_application)
                get_results_file(result_list, "all-game")
            elif act_application == "win":
                while True:
                    act_application = get_any_type("Виберіть 'user' або 'computer' або 'draw': ", "str_only_words")
                    if act_application in ["user", "computer", "draw"]:
                        break
                    print("Не правильно, повтори спробу")
                result_list = get_results_list(act_application)
                get_results_file(result_list, f"{act_application}_wins")
            elif act_application == "cho":
                while True:
                    act_application = get_any_type("Виберіть 'user' або 'computer': ", "str_only_words")
                    if act_application in ["user", "computer"]:
                        break
                    print("Не правильно, повтори спробу")
                result_list = get_results_for_choice(act_application)
                get_results_file(result_list, f"{act_application}_choice")

        else:
            break
