# list_of_numbers = [i for i in range(1, 11)]
# print(list_of_numbers)

# number = 2500

# for divisor in list_of_numbers:
#     if number % divisor == 0:
#         None
#     else:
#         return 'Failed'

def check_division(number):

    for divisor in range(1, 21):

        if number % divisor == 0:
            answer = True
        else:
            answer = False
            break

    return answer

number = 2520
while check_division(number) is not True:
    number += 2520

print(number)
# decent - don't use 'Passed' and 'Failed' as the return from the function
# though

# oh yeah true and false
# yup
# and also the for loop list could be better

# okay cool cool, i'll see!
# for loop list meaning line 13 or the actual for loop between 15 and 26?
# line 15 specifically

# hmm now for this one, out of the whole thing i didn't think 15 would be the
# issue!
# but yeah thinking

# well what's the point of line 13 at all?
# oh so i can just merge the two lines
# better :)
# i'm still not happy with your control structure, and it's the same problem
# as in 004
# we'll fix in a bit

# yep yep it didn't even feel right to write, just conveniently worked
# to give the right answer!
# yeah, i'm gonna edit your 004 in a bit to try to explain
# -> okay sure that'll be good, but do it whenever no rush!
# -> ooh could you keep a copy of my version cause i tend to forget my mistakes

# also instead of lines 22-25, you can just do
# return answer

# and even if you want to write line 22 like that, you should be using
# if not answer
# instead of
# if answer == False

# -> ah right okay that makes sense! that was a dumb if else
