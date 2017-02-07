prev, cur = 0, 1
total = 0
while cur < 4000000:
    prev, cur = cur, prev + cur
    if cur % 2 == 0:
        total += cur
print(total)
