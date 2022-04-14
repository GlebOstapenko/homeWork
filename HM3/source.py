from rich.console import Console
from rich.console import Style
console = Console()
task_list = """
1) Зформуйте строку, яка містить певну інформацію про символ в відомому слові. 
Наприклад "The [значення нокра символа] symbol in [тут слово] is '[символ з відповідним порядковим номером]'". 
Слово та номер отримайте за допомогою input() або скористайтеся константою. 
Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

2) Вести з консолі строку зі слів (або скористайтеся константою). 
Напишіть код, який визначить кількість кількість слів, в цмх даних.

3) Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 'Lorem Ipsum']. 
Напишіть механізм, який сфлрмує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1. 
Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.
==========================================================================================================="""

# Menu
task_number = "[blue]Введіть [yellow]номер[/] завдання для перевірки або '[yellow]exit[/]' для завершення перевірки дз: [/blue]"
task_check = ["1", "2", "3", "exit"]
command_error = "[red]Невідома команда, повтори спробу!!![/red]"
task_continue = ["[blue]Для продовження перевірки '[yellow]continue[/]', для завершення '[yellow]exit[/]': [/blue]",
                 ["continue", "exit"]]
thanks_check = "[green]Дякую за перевірку! [/green]"

# Task1
task_one_word = "[blue]Вкажіть [yellow]слово[/yellow] для першого завдання: [/blue]"
task_one_num = "[blue]Вкажіть [yellow]номер[/yellow] літери яку необхідно знайти: [/blue]"
task_one_error = f"[red]Не коректне число (більше довжини слова або менше 0)[/red]"

# Task2
task_second_word = "[blue]Введіть ваше [yellow]речення[/yellow] для перевірки: [/blue]"

# Task3
create_list = """[blue]Список доступних методів створення списку
[yellow]full_rand[/yellow] - цілком випадкова генерація списку
[yellow]type_rand[/yellow] - випадкове визначення типу даних у кожному пункті списку, але ручне заповнення
[yellow]value_rand[/yellow] - випадкове наповнення списку, ручна вказівка типу даних
[yellow]manual[/yellow] - повністю ручний список
Виберіть тип: [/blue]"""
type_list = ["full_rand", "type_rand", "value_rand", "manual"]
search_type = ["""[blue]Дані для формування списку
[yellow]int[/yellow] - список цілих чисел
[yellow]str[/yellow] - список рядків
[yellow]float[/yellow] - список чисел з цифрою після коми
[yellow]bool[/yellow] - список із логічних частин списку
Виберіть тип списку: [/blue]""", ["int", "str", "float", "bool"]]
task_third_result = "[green]Ваш новый список список с типом float"
