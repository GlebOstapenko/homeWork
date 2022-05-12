def args_to_str(func):
    def replacing_with_string(*args, **kwargs):
        args_string = []
        for arg in args:
            args_string.append(str(arg))
        for kwarg in kwargs:
            args_string.append(str(kwargs[kwarg]))

        return str(func(args_string))

    return replacing_with_string


@args_to_str
def get_tuple(args):
    for i in range(len(args)):
        if "4" in args[i]:
                args[i]="@$@"
    return tuple(args)


print(get_tuple(1, 2, "52", 4, "78", 8, c=2, d=4))
print(type(get_tuple(1, 2, "52", 4, "78", 8, c=2, d=4)))
