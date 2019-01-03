def count_primes(x):
    def am_i_prime(n):
        divisor = 1
        factors = []
        for _ in range(n):
            if n % divisor == 0:
                factors.append(divisor)
            divisor += 1
        if factors == [1, n]:
            return n

    number = 1
    prime_list = []
    for _ in range(x):
        y = am_i_prime(number)
        prime_list.append(y)
        number += 1

    primelist = [i for i in prime_list if i is not None]

    return primelist

print(count_primes(12))

# e.g. 12 - [2, 3, 5, 7, 11]
# check if 12/2, get 6. check again, get 3, check again, not to, check 3, get 1
# stop

# x = 12
# count_primes(x)

# if 12 % prime_list[0] == 0
#     a = rime_list[0] ^ (12 % rime_list[0])
#     print(a)
