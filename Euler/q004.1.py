list_of_products = [i * j for i in range(100, 999) for j in range(100, 999)]

def check_palindrome(number):
    number = str(number)
    return number == number[::-1]

print(check_palindrome(121))

greatest_palindrome = 0

for number in list_of_products:
    if check_palindrome(number):
        if number > greatest_palindrome:
            greatest_palindrome = number

print(greatest_palindrome)
