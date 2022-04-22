def decorator_type_variable(func):
    def decorated_result(variable):
        print(f"Тип вашої змінної - {func(variable)}")

    return decorated_result


@decorator_type_variable
def get_type_variable(variable):
    return str(type(variable))[8:-2]


s = 22, 33
get_type_variable(s)
