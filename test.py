# import re
# import random
# import all_func

n = int(input())

lst = [[1] * n] * n
lst[0][n-1] = 5

for i in lst:
    print(*i)