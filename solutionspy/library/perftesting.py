import timeit


def run(f):
    return timeit.Timer(f).timeit(number=1)


def on_range(x, f):
    def _f():
        for i in range(x):
            f(i)

    return _f
