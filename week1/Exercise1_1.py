def multiples(n):
    i = 0
    sum = 0
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            print(i)
            sum += i
        i += 1
    return sum

print(multiples(1000))
