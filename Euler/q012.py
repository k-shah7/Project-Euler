import math

def divisor_number(number):
    limit = int(math.sqrt(number))
    if math.sqrt(number) == limit:
        total = 1
        limit -= 1
        for i in range(1, limit):
            if number % i == 0:
                total += 2
    else:
        total = 0
        for i in range(1, limit):
            if number % i == 0:
                total += 2

    return total

# ha cute use of a lambda
# 'cute' it's like the ant all over again :p

# but can you think of a nicer way of doing this without needing to int
# it afterwards?

# it still works without the int, but im guessing that's not what you meant?
# integer division is probably better here
# oh right yeah!
triangle_number = lambda x: x * (x + 1) // 2

i = 1
while divisor_number(triangle_number(i)) < 500:
    i += 1

print(triangle_number(i))

