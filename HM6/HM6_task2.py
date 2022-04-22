def decorator_get_float(func):
    def decorated_result(variable):
        if (result := func(variable)) == 0:
            print("Не вдалося перетворити на float")
        else:
            print(f"Ваша змінна у форматі float - {result}")

    return decorated_result


@decorator_get_float
def get_float(variable):
    try:
        return float(variable)
    except:
        return 0


get_float("2")
