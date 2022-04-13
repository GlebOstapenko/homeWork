import all_func
import source
import re
from rich.console import Console
while True:
    print(source.task_list)
    task_number = all_func.new_check_one_in_list(source.task_number, source.task_check, source.command_error)
    if task_number == "exit":
        print("Дякую за перевірку!")
        break
    elif task_number == "1":
        while True:
            user_word = all_func.get_any_type("Вкажіть слово для завдання: ", "str_only_words")
            letter_num = all_func.get_any_type("Вкажіть номер літери: ", "int")
            result = f"Літера під номером {letter_num} у слові '{user_word}' це '{user_word[letter_num - 1]}'"
            print(result)
            task_number = all_func.new_check_one_in_list(source.task_continue[0], source.task_continue[1],
                                                         source.command_error)
            if task_number == "exit":
                break

    elif task_number == "2":
        while True:
            list_word = input("Введіть ваше речення: ")
            list_word = re.split(" ", list_word)
            result_list = []
            for word in list_word:
                word = filter(str.isalpha, word)
                word = "".join(word)
                if len(word) > 0:
                    result_list.append(word)
            print(f"Кількість слів у вашому реченні -> {len(result_list)}")
            task_number = all_func.new_check_one_in_list(source.task_continue[0], source.task_continue[1],
                                                         source.command_error)
            if task_number == "exit":
                break

    elif task_number == "3":
        while True:
            type_list = all_func.new_check_one_in_list(source.create_list, source.type_list, source.command_error)
            task_third_list = all_func.create_list(type_list)
            print("Ваш список:")
            all_func.print_list_and_type(task_third_list)
            print("=" * 50)
            user_type = all_func.new_check_one_in_list(source.search_type[0], source.search_type[1],
                                                       source.command_error)
            result_list = all_func.list_one_type(user_type, task_third_list)
            print(f"Ваш новый список список с типом {user_type}")
            all_func.print_list_and_type(result_list)
            task_number = all_func.new_check_one_in_list(source.task_continue[0], source.task_continue[1],
                                                         source.command_error)
            if task_number == "exit":
                break


