def narcissistic(value):
    power = number_of_digits(value)
    
    return sum([n**power for n in digits(value)]) == value


def digits(x):
    xs = []

    while x >= 10:
        xs.append(x % 10)
        x //= 10
    
    xs.append(x)

    xs.reverse()

    return xs


def number_of_digits(n):
    return len(digits(n))



assert digits(123) == [1, 2, 3], digits(123)
assert digits(1) == [1]

assert narcissistic(7) == True
assert narcissistic(371) == True
assert narcissistic(122) == False
assert narcissistic(4887) == False
