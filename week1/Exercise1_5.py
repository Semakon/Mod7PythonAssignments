def ispalindrome(n):
    s = str(n)
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


a, b, prod, res = 100, 100, 0, 0
ares, bres = a, b
while a < 1000:
    while b < 1000:
        prod = a * b
        if ispalindrome(prod) and prod > res:
            res = prod
            ares = a
            bres = b
        b += 1
    b = 100
    a += 1
print("ares: " + str(ares))
print("bres: " + str(bres))
print(res)
