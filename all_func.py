def get_anyType(word, search_type):
    if search_type == "float":
        while True:
            my_number = input(word)
            try:
                return (float(my_number))
            except:
                print("Ошибка, пробуй ещё раз ввести число")

    elif search_type == "int":
        while True:
            my_number = input(word)
            try:
                return (int(my_number))
            except:
                print("Ошибка, пробуй ещё раз ввести число")

    elif search_type == "str_only_words":
        while True:
            my_str = input(word)





def check_palindrome(num):
    num = str(num)
    left_bord = ""
    right_bord = ""
    centre = ""
    if int(num) < 10:
        return False
    elif len(num) % 2 == 0:
        for i in range(len(num)):
            if i < len(num) / 2:
                left_bord += num[i]
            else:
                right_bord += num[i]
        return left_bord == right_bord
    else:
        for i in range(len(num)):
            if i < (len(num) / 2) - 1:
                left_bord += num[i]
            elif i > (len(num) / 2):
                right_bord += num[i]
            else:
                centre += num[i]
        return left_bord == right_bord
