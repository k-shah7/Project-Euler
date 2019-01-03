def even(n):
    i = 1
    j = 2
    total = 2
    for _ in range(n):
        next_term = i + j
        i, j = j, next_term
        if next_term > n:
            break
        if next_term % 2 == 0:
            total += next_term
    return total


# Two ways of calculating fibonacci numbers
def fib(n):
    print("Called fib({0})".format(n))
    if n < 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(2)

# def fib2(n):
#     a = 1
#     b = 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a


# Here's a test to confirm they both return the right answers
# for k in range(10):
#     print(k, fib(k), fib2(k))

# Which of the two ways is better?


# print(even(4000000))
# print(even(10))
