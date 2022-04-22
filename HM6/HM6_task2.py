def get_float(variable):
    try:
        print(f"Ваша змінна у форматі float - {float(variable)}")
        return float(variable)
    except:
        print("Не вдалося перетворити на float")
        return 0


var = [2]
result = get_float(var)
