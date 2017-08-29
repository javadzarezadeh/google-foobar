import math


def answer(n):
    l = [math.floor(n / 2), math.ceil(n / 2)]
    return create_lists(l)


def validate(l):
    list_is_ordered_truely = all(l[i] <= l[i + 1] for i in range(len(l) - 1))
    list_is_added_less_than_one = all(l[i + 1] - l[i] <= 1 for i in range(len(l) - 1))
    first_element_is_one = l[0] == 1
    if list_is_added_less_than_one and list_is_ordered_truely and first_element_is_one:
        return True
    return False


final_list = []


def create_lists(l):
    l.sort()
    if validate(l):
        final_list.extend(l)
    if l[-1] > 1:
        l[-1] -= 1
        l.append(1)
        create_lists(l)


answer(5)
print(final_list)
