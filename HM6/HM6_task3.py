def task3(variable1, variable2):
    if type(variable1) == int and type(variable2) == int:
        return task3_numbers(variable1, variable2)
    elif type(variable1) == str and type(variable2) == str:
        return task3_string(variable1, variable2)
    elif type(variable1) == str:
        return task3_dict(variable1, variable2)
    else:
        return task3_other_type(variable1, variable2)


def task3_numbers(number1, number2):
    if number1 == number2:
        print(f"Змінні рівні")
        return 0
    number1, number2 = min(number1, number2), max(number1, number2)
    result = number1 - number2
    print(f"Різниця змінних - {result}")
    return result


def task3_string(string1, string2):
    result = string1 + string2
    print(f"Ваша нова строка - '{result}'")
    return result


def task3_dict(string, variable):
    result = {string: variable}
    print(f"Ваш новий словник - '{result}'")


def task3_other_type(variable1, variable2):
    result = tuple([variable1, variable2])
    print(f"Ваш новий кортеж - {result}")
    return result


task3(2, 2)
task3("2", "2")
task3("2", 2)
task3(2, "2")
print(type(task3([2], {2})))
