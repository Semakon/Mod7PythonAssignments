def gcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a


def frac(a, b):
    if b == 0:
        return "Second argument ('b') cannot be 0."
    # a, b = abs(a), abs(b)
    c = gcd(a, b)
    if a < 0 and b < 0:
        a, b, = abs(a), abs(b)
    return a // c, b // c


# bullet point 1
print(gcd(3141, 156))


# bullet point 2
print(gcd(12345678, 987654321))


# bullet point 3
print(frac(3141, 156))
print(frac(-8, 12))
print(frac(8, -12))
print(frac(-8, -12))
