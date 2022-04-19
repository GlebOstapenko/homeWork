# import re
# import random
# import all_func

def decor_test(func):
    def is_adm(password):
        if password == "qwert":
            return func
            # return func()
    return is_adm


# @decor_test
def is_admin():
    return "You admin"


test = decor_test(is_admin())
# print(is_admin("qwert"))
print(test("qwefrt"))
