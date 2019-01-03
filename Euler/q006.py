sum_of_squares = sum(i ** 2 for i in range(1, 101))
# print(sum_of_squares)

square_of_sums = sum(i for i in range(1, 101)) ** 2
# print(square_of_sums)

difference = square_of_sums - sum_of_squares
# print(difference)
# ahhh so, so close to perfect!
# oh hi!
# hey :)

# :)
# where's the mistake?
# line 1

# oh lol okay, im thinking!
# so close though
# i'm just gonna tell you because it's subtle
# change from a list comp to a generating expression
# nope
# very nope
# uh oh!!
# what's the point in making a list?
# all you care about is the sum
# you just needed to change what line 1 used to be
# (line 206 of comprehensions)

# ah oh yeah the same thing again i keep on making lists!
# done?
# cool!
# some pointless brackets in line 4 but otherwise good :)
# :)
# good work :)
# was a very easy one to be fair, but :)

def slow(n):
    sum_of_squares = sum(i**2 for i in range(n+1))
    square_of_sums = sum(range(n+1))**2
    return square_of_sums - sum_of_squares

# print(question6(100))

# nice!
# wasn't expecting line 39 to work tbh
# but just realised - this solution isn't perfect!
# can you think of a better maths way of doing this? :)
# like I can't fault your implementation of the algorithm
# but is there a better algorithm

# yeah i think there is, let me try and write it!
# good girl :)

def fast(n):
    sum_of_squares = (n * (n + 1) * (2 * n + 1)) // 6
    square_of_sums = ((n * (n + 1)) // 2) ** 2
    return square_of_sums - sum_of_squares

# print(question6_2(100))

# done!

import time
print(' | '.join(['{:^20}', '{:^15}', '{:^15}']).format('n', 'slow', 'fast'))
print('+'.join(['-'*21, '-'*17, '-'*16]))

for k in range(9):
    n = 10**k
    print('{:>20}'.format(n), end='', flush=True)

    for function in [slow, fast]:
        print(' | ', end='', flush=True)
        start = time.time()
        function(n)
        duration = time.time() - start
        print("{:15.5f}".format(duration), end='', flush=True)
    print()

# on my machine, k=10 would take an hour
# ooh woah i just saw this! so cool the way you've formatted it
# lol lets not to k = 10 then!

# yeah! wanted to demonstrate the time difference between the two methods
print()
print(' | '.join(['{:^20}', '{:^15}']).format('n', 'fast'))
print('+'.join(['-'*21, '-'*17]))

for p in range(10):
    k = 10**p
    n = 2**k

    print('{:>20} | '.format('2^'+str(k)), end='', flush=True)
    start = time.time()
    function(n)
    duration = time.time() - start
    print("{:15.5f}".format(duration), end='', flush=True)
    print()
