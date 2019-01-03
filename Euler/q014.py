def even(number):
    return number // 2

def odd(number):
    return (3 * number) + 1

def collatz_sequence(start):
    count = 1
    current_number = start
    # print(current_number)
    while current_number > 0:
        if current_number == 1:
            break
        if current_number % 2 == 0:
            current_number = even(current_number)
            count += 1
            # print(current_number)
        else:
            current_number = odd(current_number)
            count += 1
            # print(current_number)

    return count


max_count = 0
start_number = 0
for i in range(100000, 1000001):
    if collatz_sequence(i) > max_count:
        max_count = collatz_sequence(i)
        start_number = i

print(max_count, start_number)

# too slow
