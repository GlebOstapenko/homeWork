def task3_get_numbers(number1, number2):
    number1, number2 = max(number1, number2), min(number1, number2)
    result = number1 - number2
    return result


def task3_get_string(string1, string2):
    result = string1 + string2
    return result


def task3_get_dict(string, variable):
    result = {string: variable}
    return result


def task3_get_tuple(variable1, variable2):
    result = variable1, variable2
    return result


def get_type_decorator(func):
    def get_type(variable1, variable2):
        var_and_type = [variable1, variable2]
        if type(variable1) == type(variable2) == int:
            var_and_type.append(int)
        elif type(variable1) == type(variable2) == str:
            var_and_type.append(str)
        elif type(variable1) == str:
            var_and_type.append(dict)
        else:
            var_and_type.append(tuple)
        return func(var_and_type)

    return get_type


def result_decorator(func):
    def result_text(variable1, variable2):
        result = func(variable1, variable2)
        if type(result) == int:
            if result == 0:
                return "Числа однакові"
            else:
                return f"Різниця - {result}"
        elif type(result) == str:
            return f"Отримана строка - {result}"
        elif type(result) == dict:
            return f"Отриманий словник - {result}"
        else:
            return f"Отриманий кортеж - {result}"

    return result_text


@result_decorator
@get_type_decorator
def task3(variables):
    if variables[2] == int:
        return task3_get_numbers(variables[0], variables[1])
    elif variables[2] == str:
        return task3_get_string(variables[0], variables[1])
    elif variables[2] == dict:
        return task3_get_dict(variables[0], variables[1])
    else:
        return task3_get_tuple(variables[0], variables[1])


print(task3(2, 4))
print(task3("2", "2"))
print(task3("2", 2))
print(task3(2, "2"))
