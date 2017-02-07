def divisors(a):
    a = abs(a)
    n = a
    if n == 1:
        return {1}
    res = {1, n}
    i = 2
    while i < n:
        if a % i == 0:
            res.add(i)
            temp = a // i
            res.add(temp)
            n = temp
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
        if n <= 1:
            break
    return res


# bullet point 1
print(divisors(147))
print(divisors(13195))


# bullet point 2
print(primefact(147))
print(primefact(13195))
