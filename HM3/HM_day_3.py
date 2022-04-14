import all_func
import source
import re
from rich.console import Console
from rich.console import Style

console = Console()
while True:
    print(source.task_list)
    task_number = all_func.new_check_one_in_list(source.task_number, source.task_check, source.command_error)
    if task_number == "exit":
        console.print(source.thanks_check)
        break
    elif task_number == "1":
        while True:
            user_word = all_func.get_any_type(source.task_one_word, "str_only_words")
            while True:
                letter_num = all_func.get_any_type(source.task_one_num, "int")
                if letter_num > 0 and letter_num <= len(user_word):
                    break
                else:
                    console.print(source.task_one_error)
            result = f"Літера під номером [blue]{letter_num}[/] у слові '[blue]{user_word}[/]' це " \
                     f"'[blue]{user_word[letter_num - 1]}[/]'"
            console.print(result, style="green")
            task_number = all_func.new_check_one_in_list(source.task_continue[0], source.task_continue[1],
                                                         source.command_error)
            if task_number == "exit":
                break

    elif task_number == "2":
        while True:
            list_word = console.input(source.task_second_word)
            list_word = re.split(" ", list_word)
            result_list = []
            for word in list_word:
                word = filter(str.isalpha, word)
                word = "".join(word)
                if len(word) > 0:
                    result_list.append(word)
            console.print(f"Кількість слів у вашому реченні -> [blue]{len(result_list)}[/]",style="green")
            task_number = all_func.new_check_one_in_list(source.task_continue[0], source.task_continue[1],
                                                         source.command_error)
            if task_number == "exit":
                break

    elif task_number == "3":
        while True:
            type_list = all_func.new_check_one_in_list(source.create_list, source.type_list, source.command_error)
            task_third_list = all_func.create_list(type_list)
            console.print("[green]Ваш список:[/green]")
            all_func.print_list_and_type(task_third_list)
            print("=" * 50)
            user_type = all_func.new_check_one_in_list(source.search_type[0], source.search_type[1],
                                                       source.command_error)
            result_list = all_func.list_one_type(user_type, task_third_list)
            console.print(f"[green]Ваш новий список з типом[/green] [blue]{user_type}[/blue]")
            all_func.print_list_and_type(result_list)
            task_number = all_func.new_check_one_in_list(source.task_continue[0], source.task_continue[1],
                                                         source.command_error)
            if task_number == "exit":
                break
