
# alright so your *idea* makes sense
# and you've done it in a not entirely stupid way

def check_palindrome2(number):
    number = str(number)
    return number == number[::-1]

print(check_palindrome2(121))
print(check_palindrome2(12145))


# def check_palindrome(number):
#     number = str(number)
#     length = len(number)
#     py_length = length - 1
#     # print(range(palin_range_even))
#     if py_length % 2 == 1:  # if even
#         palin_range = length // 2
#         for i in range(palin_range):
#             # print(i)
#             number_pair = (py_length) - i
#             if number[i] == number[number_pair]:
#                 # print(number[i], number[number_pair])
#                 result = True
#             else:
#                 # print(number[i], number[number_pair])
#                 return False

#     elif py_length == 0:
#         return True

#     else:  # if odd
#         palin_range = (length - 1) // 2
#         for i in range(palin_range):
#             # print(i)
#             number_pair = (py_length) - i
#             if number[i] == number[number_pair]:
#                 # print(number[i], number[number_pair])
#                 result = True
#             else:
#                 # print(number[i], number[number_pair])
#                 return False

#     return result

# # print(check_palindrome(1134511))  # not palin
# # print(check_palindrome(1235321))  # palin
# # print(check_palindrome(1235324))  # not palin

# # linter is yelling that the line is too long
# # but great idea here :) - just taken from your comprehensions :P
# # you're a good learner then :)
# # :) :)
# list_of_products = [(i, j, i * j) for i in range(1, 999) for j in range(1, 999) if check_palindrome(i * j) == True]

# # why did you set it?
# # cause there are repeats e.g. 900 * 910 and 910 * 900 will both come up
# # idek if they're palindroms but cause of that
# # alright so there are repeats, do they matter?
# # no just thought it was nicer
# # haha okay fair enough
# list_of_palindromes = sorted(list(set([value[2] for value in list_of_products])))

# # we'll cover set comprehensions when you're back too

# # list_of_palindromes = []
# # for i in list_of_products:
# #     check_palindrome(i)
# #     check = check_palindrome(i)
# #     if check == 'palindrome':
# #         list_of_palindromes.append(i)

# print(list_of_products)
# print(list_of_palindromes)

# # issue why does range(1, 999) not work

# # what do you mean not work?
# # if you change line 36 to range(1, 999) it doesn't work - only works from
# # range(5, _) onwards
