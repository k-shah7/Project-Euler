def check_prime(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)

    if len(factors) == 2:
        return True

    else:
        return False

for number in range(1, 600851475143 + 1):
    if 600851475143 % number == 0:
        if check_prime(number):
            print(number)
