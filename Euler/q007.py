# def check_prime(number):
#     if number == 1:
#         return False
#     else:
#         for i in range(2, number):
#             if number % i == 0:
#                 answer = False
#                 break
#             else:
#                 answer = True

#     return answer


# def generate_primes(limit):
#     def check_prime(number):
#         for i in range(2, number):
#             if number % i == 0:
#                 answer = False
#                 break
#             else:
#                 answer = True

#         return answer
#     prime_list = []
#     for number in range(2, 1000):
#         # prime_list = [number if check_prime(number) is True]
#         if check_prime(number) is True:
#             prime_list.append(number)

#     return prime_list

# generate_primes(12)

def check_prime(number):
    if number is 2:
        return True

    else:

        for i in range(2, number):
            if number % i == 0:
                return False
            else:
                answer = True

        return answer


# for number in range(2, 100):
#     if check_prime(number) is True:
#         print(number)

def generate_primes(limit):
    number = 2
    count = 0
    while count != limit:
        if check_prime(number) is True:
            count += 1
        number += 1
    return count, (number - 1)

print(generate_primes(34))

# very slow - 135.7

# def generate_primes(limit):
#     if limit == 1:
#         return 1, 2
#     else:
#         number = 3
#         count = 2
#         while count != limit:
#             if check_prime(number) is True:
#                 count += 1
#             number += 2
#         return count, (number - 1)

# print(generate_primes(10001))
 # just wrong
