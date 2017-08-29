def answer(x, y):
    sum1 = 0
    for i in range(1, x + 1):
        sum1 += i
    for j in range(x, x + y-1):
        sum1 += j
    return sum1


print(answer(4, 2))