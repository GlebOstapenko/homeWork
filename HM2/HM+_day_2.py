import all_func

user_list = {"admin": ["qwert1234", "Gleb", "Ostapenko", 22],
             "user": ["qwert", "Daniel", "Kronov", 15]}

film_list = {"Avengers": ["Длительность в минутах - 143", "Возрастное ограничение - 12 лет", 12],
             "Saw": ["Длительность в минутах - 103", "Возрастное ограничение - 18 лет", 18]}
while True:
    # Login===============================================
    user_login = ""
    while True:
        user_login = all_func.get_any_type("""Желаете пройти регистрацию, или залогиниться в существующий аккаунт?
login - для авторизации
registry - для регистрации
exit - завершить программу
Введите команду: """, "str_only_words")
        if all_func.check_one_in_list(user_login, ["login", "registry", "exit"]):
            break
        else:
            print("Неизвестная команда, попробуйте ещё раз!\n")
    if user_login == "exit":
        break
    while True:
        if user_login == "login":
            user_login = all_func.check_user_login(user_list)
            break

        if user_login == "registry":
            new_user = ["", "", "", 0]
            while True:
                user_login = input("Введите логин для нового аккаунта: ")
                if user_login in user_list:
                    print("Логин занят")
                else:
                    break
            new_user[0] = input("Введите пароль для нового аккаунта: ")
            new_user[1] = all_func.get_any_type("Введите ваше имя: ", "str_only_words").capitalize()
            new_user[2] = all_func.get_any_type("Введите вашу фамилию: ", "str_only_words").capitalize()
            while True:
                new_user[3] = all_func.get_any_type("Введите ваш возраст: ", 'int')
                if new_user[3] < 0:
                    print("Как ты растёшь в минус?) Укажи, пожалуйста, адекватный возраст")
                else:
                    break
            user_list.update({user_login: new_user})
            break

    # Admin===============================================================================================
    if user_login == "admin":
        admin_act = ""
        while True:
            while True:
                admin_act = all_func.get_any_type("""Укажите, необходимые действия:
check - просмотретть весь список фильмов
add - добавить фильм
delete - удалить фильм
correct - изменить информацию о фильме
exit - выйти из аккаунта админа
Введите команду: """, "str_only_words")

                if all_func.check_one_in_list(admin_act, ["check", "add", "delete", "correct", "exit"]):
                    break
                else:
                    print("Неизвестная команда, попробуйте ещё раз!\n")
            if admin_act == "exit":
                print("=================================")
                break
            elif admin_act == "add":
                new_film = all_func.get_any_type("Введите название нового фильма: ", "str_only_words").capitalize()
                film_duration = 0
                while True:
                    film_duration = all_func.get_any_type("Введите длительность фильма в минутах: ", "int")
                    if film_duration > 0:
                        break
                    else:
                        print("Фильм с отрицательным временем не может быть")
                age_limit = 0
                while True:
                    age_limit = all_func.get_any_type("Введите возрастное ограничение фильма: ", "int")
                    if age_limit < 65 and age_limit > 0:
                        break
                    else:
                        print("Для кого этот фильм? Поставь нормальный возрат ( < 65 лет)")
                film_list.update({new_film: [f"Длительность в минутах - {film_duration}",
                                             f"Возрастное ограничение - {age_limit} лет", age_limit]})

            elif admin_act == "delete":
                while True:
                    admin_act = all_func.get_any_type("Введите название фильма который нужно удалить: ",
                                                      "str_only_words").capitalize()
                    if admin_act in film_list:
                        film_list.pop(admin_act)
                        print(f"Фильм {admin_act} успешно удалён")
                        break
                    else:
                        print("Нет такого фильма в списке")


            elif admin_act == "correct":
                while True:
                    correct_film = all_func.get_any_type("Введите название фильма для корректировки: ",
                                                         "str_only_words").capitalize()
                    if correct_film in film_list:
                        break
                    else:
                        print("Такого фильма нет в системе, попробуй ещё")

                while True:
                    admin_act = all_func.get_any_type("""Поле доступные для редактирования:
time - длительность фильма
age - возрастное ограничение
Введите необходимы параметр для изменения:""", "str_only_words")
                    if all_func.check_one_in_list(admin_act, ["time", "age"]):
                        break
                    else:
                        print("Неизвестная команда, попробуйте ещё раз!\n")

                if admin_act == "time":
                    new_time = 0
                    while True:
                        new_time = all_func.get_any_type("Укажите новую длительность сеанса: ", "int")
                        if new_time > 0:
                            break
                        else:
                            print("Фильм с отрицательным временем не может быть")
                    film_list[correct_film][0] = f"Длительность в минутах - {new_time}"
                else:
                    new_age = 0
                    while True:
                        new_age = all_func.get_any_type("Укажите укажите новое возратсное ограничение:  ", "int")
                        if new_age < 65 and new_age > 0:
                            break
                        else:
                            print("Для кого этот фильм? Поставь нормальный возрат ( < 65 лет)")
                    film_list[correct_film][1] = f"Возрастное ограничение - {new_age} лет"
                    film_list[correct_film][2] = new_age
            else:
                all_func.check_dict(film_list, 2)

    # USER=============================================================================
    else:
        user_action = ""
        while True:
            while True:
                user_action = all_func.get_any_type("""Доступные действия 
check - просмотреть список фильмов
buy - купить билет
exit - выйти из аккаунта
Выберите необходимое дейтсиве: """, "str_only_words")
                if all_func.check_one_in_list(user_action, ["check", "buy", "exit"]):
                    break
                else:
                    print("Неизвестная команда, попробуйте ещё раз!\n")

            if user_action == "check":
                all_func.check_dict(film_list, 2)
            elif user_action == "exit":
                break
            else:
                while True:
                    film = all_func.get_any_type("Введите название фильма: ", "str_only_words").capitalize()
                    if film in film_list:
                        break
                    else:
                        print("Нет такого фильма, попробуй ещё")

                if user_list[user_login][3] < 7:
                    print("Где твои родители?")
                elif user_list[user_login][3] < film_list[film][2]:
                    if all_func.check_palindrome(user_list[user_login][3]):
                        print("Какой прекрасный возвраст, но это фильм для взрослых!")
                    else:
                        print("Это фильм для взрослых!")
                elif user_list[user_login][3] >= 65:
                    if user_list[user_login][3] > 122:
                        print("По вам книга рекордов Гинесса плачет")
                    if all_func.check_palindrome(user_list[user_login][3]):
                        print("У вас прекрасный возвраст, пожалуйста, покажите пенсионное удостоверение!")
                    else:
                        print("Пожалуйста, покажите пенсионное удостоверение!")
                else:
                    if all_func.check_palindrome(user_list[user_login][3]):
                        print("У вас прекрасный возвраст, но нужно было приходить раньше, билетов больше нет!")
                    else:
                        print("Нужно было приходить раньше, билетов больше нет!")
