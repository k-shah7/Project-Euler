import math

def check_prime(number):
    if number is 2: # should use == for comparison to integers
        return True

    else:

        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                answer = True

        return answer

# current_total = 2

# for number in range(3, 2000001, 2):
#     if check_prime(number):
#         current_total += number

# print(current_total)

# too slow

def check_prime2(number):
    if number == 2 or number == 3:
        return True

    elif number % 2 == 0 or number % 3 == 0:
        return False

    else:
        limit = int(number ** 0.5) + 1
        for i in range(5, limit, 2):
            if number % i == 0:
                return False

        return True
# was check_prime2 faster than check_prime?
# way faster, i never even got an answer with check_prime
# oh! didn't realise lines 35/36 were different
# yeah that makes sense
# it's still a bit slow though - research other ways to make a list of prime numbers

# there's stuff about how numbers can be written as 6k +/- 1, which
# i didn't bother looking at properly, but yeah will do!

# not checking if a number is prime - generating a list of primes

# yeah still do this when you get a chance

# print(check_prime2(87))

current_total = 2

for number in range(3, 2000000, 2):
    if check_prime2(number):
        current_total += number

print(current_total)
