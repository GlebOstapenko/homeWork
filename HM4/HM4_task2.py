import all_func

"""
2) Є два довільних числа які відповідають за мінімальну і максимальну ціну.
Є Dict з назвами магазинів і цінами: { "cito": 47.999, "BB_studio" 42.999, "momo": 49.999, "main-service": 37.245,
"buy.now": 38.324, "x-store": 37.166, "the_partner": 38.988, "sota": 37.720, "rozetka": 38.003}. Напишіть код,
який знайде і виведе на екран назви магазинів, ціни яких попадають в діапазон між мінімальною і максимальною ціною.
"""

task_dict = {"cito": 47.999,
             "BB_studio": 42.999,
             "momo": 49.999,
             "main-service": 37.245,
             "buy.now": 38.324,
             "x-store": 37.166,
             "the_partner": 38.988,
             "sota": 37.720,
             "rozetka": 38.003}

task_min = all_func.get_any_type("Введите минимальную сумму: ", "float")
while True:
    task_max = all_func.get_any_type("Введите максимальную сумму: ", "float")
    if task_max < task_min:
        print("Сумма меньше минимальной, попробуй ещё")
        continue
    break
res_lst = []
for shop in task_dict:
    if task_dict[shop] >= task_min and task_dict[shop] <= task_max:
        res_lst.append(shop)
print(f"Список магазинов которые подходят: {res_lst}" )
