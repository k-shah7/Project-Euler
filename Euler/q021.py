import math

def factor_sum(number):
    number_range = int(math.sqrt(number))
    factor_list = set()
    for factor in range(1, number_range + 1):
        if number % factor == 0:
            factor_list.add(factor)
            factor_list.add(number // factor)

    return sum(factor_list) - number

# print(factor_sum(220))

def check_aimable(a):
    """True if factor_sum(a) = b and factor_sum(b) = a"""
    b = factor_sum(a)
    if b == a:
        return False

    elif factor_sum(b) == a:
        return True

    else:
        return False

amiable_list = []

for number in range(10000):
    if check_aimable(number):
        aimable_list.append(number)

print(sum(aimable_list))
