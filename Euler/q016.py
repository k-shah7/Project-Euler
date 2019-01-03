number = str(2 ** 1000)
print(number)
total = 0

for i in range(len(number)):
    print(number[i])
    total += int(number[i])

print(total)


