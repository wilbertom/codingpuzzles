# https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/python

from .lib.digits import digits


def narcissistic(value):
    power = number_of_digits(value)

    return sum([n ** power for n in digits(value)]) == value


def number_of_digits(n):
    return len(digits(n))
