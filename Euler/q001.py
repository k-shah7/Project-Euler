def method1(n):
    total = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            total += i

    return total


def method2(n):
    return sum(i for i in range(n) if (i % 3 == 0) or (i % 5 == 0))


def method3(n):
    def helper(divisor, n):
        sum_to = (n - 1) // divisor
        return divisor * sum_to * (sum_to + 1) // 2

    return (helper(3, n) + helper(5, n)) - helper(15, n)


print(method1(1000))
print(method2(1000))
