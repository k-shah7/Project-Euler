import math

def check_square(number):
    return math.sqrt(number).is_integer()

def check_answer(pt):
    if pt[0] + pt[1] + pt[2] == 1000:
        return True
    else:
        return False

list_numbers = [(i, j, int(math.sqrt(i**2 + j**2))) for i in range(1, 1000) for j in range(1, 1000) if check_square((i**2 + j**2))]

for pt in list_numbers:
    if check_answer(pt):
        print(pt)
        print(pt[0] * pt[1] * pt[2])

# fix 004 when you can
# oh yeah forgot about that one, will do!
# good girl :)
