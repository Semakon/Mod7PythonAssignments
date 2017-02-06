def encode(n):
    if n < 0 or n > 35:
        return "Please give a number between 0 (inclusive) and 35 (inclusive)"
    if 0 <= n <= 9:
        return str(n)
    return chr(n + 55)


def to_k(n, k):
    if n < 0 or k < 2 or k > 35:
        return "n should be positive and k should be between 2 (inclusive) and 35 (inclusive)"
    if k == 10:
        return str(n)
    n2 = n
    s = ""
    while n2 > k:
        q = n2 // k
        r = n2 % k
        s = encode(r) + s
        n2 = q
    if n2 == k:
        s = str(10) + s
    else:
        s = encode(n2) + s
    return s


def decode(s):
    n = ord(s)
    if 48 <= n <= 57:
        return n - 48
    n -= 55
    if n < 0 or n > 35:
        return "Please give a string with one number (0-9) or one letter (A-Z)"
    return n


def from_k(s, k):
    if k < 2 or k > 35:
        return "k should be between 2 (inclusive) and 35 (inclusive)"
    i = 0
    n = len(s) - 1
    res = 0
    while i < len(s):
        d = decode(s[i])
        res += d * (k ** n)
        i += 1
        n -= 1
    return res


def convert(k, m, s):
    return to_k(from_k(s, k), m)


# bullet point 1
print(encode(0))
print(encode(35))


# bullet point 2
print(to_k(4321, 16))
print(to_k(317547, 16))


# bullet point 3
print(decode("Z"))
print(decode("0"))
print(decode("9"))


# bullet point 4
print(from_k("10E1", 16))
print(from_k("4D86B", 16))


# bullet point 5
print(convert(16, 7, "B48C03"))
print(convert(2, 4, "10011010"))
