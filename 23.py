from math import ceil
def c(a, b):
    if a == b:
        return 1
    if a < b:
        return 0
    if a == 26 or a == 30:
        return 0
    return c(a - 3, b) + c(ceil(a / 2), b)

print(c(69, 14))
