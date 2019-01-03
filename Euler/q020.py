def factorial(n):
    if n == 0:
        return 1

    else:
        return n * factorial(n - 1)


number = str(factorial(100))
total = 0
for digit in number:
    total += int(digit)

print(total)
