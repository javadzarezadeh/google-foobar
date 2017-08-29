def answer(l, t):
    # your code here
    start_idx = 0
    end_idx = len(l)
    sum1 = 0
    while start_idx < len(l):
        for i in range(start_idx, end_idx):
            sum1 += l[i]
            # print(sum1)
            if sum1 == t:
                return [start_idx, i]
        start_idx += 1
        sum1 = 0
    return [-1, -1]


answer([4, 3, 10, 2, 8], 12)
