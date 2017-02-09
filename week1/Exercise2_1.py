from week1.perm import *


def composition(p, q):
    comp = p[:]
    for i in range(len(p)):
        comp[i] = q[p[i]]
    return comp


def inverse(p):
    inv = p[:]
    for i in range(len(p)):
        inv[p[i]] = i
    return inv


def power(p, i):
    pwr = p[:]
    if i == 0:
        pwr = composition(inverse(pwr), p)
    elif i > 0:
        j = 0
        while j < i:
            pwr = composition(pwr, p)
            j += 1
    else:
        j = 0
        pwr = composition(pwr, inverse(p))
        while j < i:
            pwr = composition(inverse(pwr), inverse(p))
            j += 1
    return pwr


def period(p):
    i = 1
    while True:
        if is_trivial(power(p, i)):
            return i
        i += 1


p = test_permutation(20)
print("p: " + str(p))
print("i: " + str(period(p)))
