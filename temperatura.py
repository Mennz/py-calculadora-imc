def celsius_para_fahrenheit(c):
    return c * 9 / 5 + 32


# 273.15 é o zero absoluto em kelvin
def celsius_para_kelvin(c):
    return c + 273.15


def fahrenheit_para_celsius(f):
    return (f - 32) * 5 / 9


def kelvin_para_celsius(k):
    return k - 273.15
