import time


def func_work_time(func):
    def get_work_time(iter_count, stop_time=0):
        start_time = time.time()
        res = func(iter_count, stop_time)
        finish_time = time.time()
        print(f"{finish_time - start_time}")
        return res

    return get_work_time


@func_work_time
def get_fib_list(iter_count, stop_time=0):
    result = [0, 1]
    time.sleep(stop_time)
    for i in range(iter_count):
        result.append(result[-1] + result[-2])

    return result


get_fib_list(iter_count=1000, stop_time=5)
