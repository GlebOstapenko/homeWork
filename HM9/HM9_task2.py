def get_type(arg_type):
    def decorator(func):
        def wrap(arg):
            return arg_type(func(arg_type(arg)))
        return wrap
    return decorator

@get_type(str)
def get_str_len(my_str):
    return len(my_str)

print(get_str_len({"s":1}))
print(type(get_str_len(123456)))