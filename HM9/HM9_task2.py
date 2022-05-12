def args_to_str(func):
    def replacing_with_string(*args):
        args_string = []
        for arg in args:
            args_string.append(str(arg))
        return func(args_string)
    return replacing_with_string


@args_to_str
def get_str(args):
    result_str = " ".join(args)
    return result_str


print(get_str(1,2,"52",4,"78",8))