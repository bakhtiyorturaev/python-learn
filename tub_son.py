def tub_son(n):
    tub = []

    for i in n:
        res = 0
        for j in range(1, i + 1):
            if i % j == 0:
                res += 1
        if res == 2:
            tub.append(i)
    return tub


numbers = range(1, 100 + 1)
print(tub_son(numbers))
