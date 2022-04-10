import all_func

user_list = {"admin": ["qwert1234", "Gleb", "Ostapenko", 22],
             "user": ["qwert", "Daniel", "Kronov", 15]}

film_list = {"Avengers": [143, 12],
             "Saw": [103, 18]}

while True:
    # Login===============================================
    user_login = ""
    while True:
        user_login = all_func.get_anyType("""Желаете пройти регистрацию, или залогиниться в существующий аккаунт?
login - для авторизации
registry - для регистрации
Введите команду: """, "str_only_words")
        if all_func.check_one_in_list(user_login, ["login", "registry"]):
            break
        else:
            print("Неизвестная команда, попробуйте ещё раз!\n")
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
            new_user[1] = all_func.get_anyType("Введите ваше имя: ", "str_only_words").capitalize()
            new_user[2] = all_func.get_anyType("Введите вашу фамилию: ", "str_only_words").capitalize()
            new_user[3] = all_func.get_anyType("Введите ваш возраст: ", 'int')
            user_list.update({user_login: new_user})
            break
    if user_login == "admin":
        admin_act = ""
        while True:
            while True:
                admin_act = all_func.get_anyType("""Укажите, необходимые действия:
checkFilm - просмотретть весь список фильмов
checkUser - посмотреть список порльзователей
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
                break
            elif admin_act == "add":
                new_film = all_func.get_anyType("Введите название нового фильма: ", "str_only_words").capitalize()
                film_duration = all_func.get_anyType("Введите длительность фильма в минутах: ", "int")
                age_limit = all_func.get_anyType("Введите возрастное ограничение фильма: ", "int")
                film_list.update({new_film:[film_duration,age_limit]})
            elif admin_act == "delete":
                admin_act = all_func.get_anyType("Введите название фильма который нужно удалить: ",
                                                 "str_only_words").capitalize()
                film_list = all_func.delete_tile_list(admin_act,film_list)
                print(f"Фильм {admin_act} успешно удалён")


