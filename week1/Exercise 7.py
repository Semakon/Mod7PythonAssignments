from collections import defaultdict


def divisors(a):
    a = abs(a)
    if a == 1:
        return {1}
    res = {1, a}
    i = 2
    while i < a:
        if a % i == 0:
            res.add(i)
        i += 1
    return sorted(res)


def isprime(a):
    return len(a) == 2


# Expensive
def primefact(a):
    res = dict()
    n = a
    while True:
        div = divisors(n)
        if isprime(div):
            if res.get(n) is not None:
                res[n] += 1
            else:
                res[n] = 1
            break
        for i in div:
            if isprime(divisors(i)):  # i is prime
                if res.get(i) is not None:
                    res[i] += 1
                else:
                    res[i] = 1
                n = n // i
    return res


# bullet point 1
print(divisors(147))


# bullet point 2
print(primefact(147))