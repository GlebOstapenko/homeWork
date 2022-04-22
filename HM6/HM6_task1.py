def get_type_variable(variable):
    result = str(type(variable))[8:-2]
    print(f"Тип вашої змінної - {result}")



var = (222)
get_type_variable(var)