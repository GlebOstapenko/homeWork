import csv
from datetime import datetime
from all_func import get_any_type


def get_results_file(results_list, list_type):
    user_acr = get_any_type("Бажаєте завантажити файл? ('yes' - так 'інше значення' - ні) : ", "str_only_words")
    if user_acr == "yes":
        game_datetime = str(datetime.now())[:-7].replace(" ", "_").replace(":", "-")
        file_name = f"{list_type}_{game_datetime}.csv"
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(("game_number", "user_choice", "computer_choice", "winner", "game_datetime"))
            for result in results_list:
                writer.writerow(result)
