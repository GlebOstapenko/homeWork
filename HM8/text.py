choice_list = "rock", "paper", "scissors", "lizard", "spock"
rules = {"rock": ["lizard", "scissors"],
         "paper": ["rock", "spock"],
         "scissors": ["lizard", "paper"],
         "lizard": ["spock", "paper"],
         "spock": ["scissors", "rock"]}
main_menu = """     Menu
[game] - зіграти у гру
[res] - переглянути списки з результатами
будь-яке інше значення - вийти з програми"""

res_menu = """    Result list filter
[all] - результат усіх ігор
[win] - за переможцем
[cho] - по вибраному ходу
будь-яке інше значення – вийти в головне меню"""