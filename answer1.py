def answer(s):
    # your code here
    l = 1
    while len(s) > l:
        print(l)
        result_bool = True
        result_int = 0
        for i in range(0, len(s) - l + 1, l):
            if s[i:i + l] != s[0:l]:
                result_bool = False
                print(s[i:i + l])
                break
            else:
                result_int += 1
        if result_bool is True and result_int * l == len(s):
            return int(len(s) / l)
        else:
            l += 1

    return 1


print(answer('aabbaaabbaaabba'))