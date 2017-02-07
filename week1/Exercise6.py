def fact(n):
    if n < 1:
        return "n should be 1 or higher"
    if n == 1:
        return 1
    return n * fact(n - 1)


def binom(n, k):
    if n < 1 or k > n:
        return "n >= 1 and n >= k >= 1"
    return fact(n) // (fact(n - k) * fact(k))


# bullet point 1
print(fact(28))


# bullet point 2
print(binom(12, 8))
print(binom(40, 2))
