from .narcissistic_number import narcissistic


def test_narcissistic():
    assert narcissistic(7) is True
    assert narcissistic(371) is True
    assert narcissistic(122) is False
    assert narcissistic(4887) is False
