def digits_mod_div_reverse(x):
    xs = []

    while x >= 10:
        xs.append(x % 10)
        x //= 10

    xs.append(x)

    xs.reverse()

    return xs


def digits_str_list(x):
    return [int(d) for d in str(x)]


digits = digits_mod_div_reverse
