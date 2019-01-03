list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.remove('Biology')
print("list now : ", list1)
list1.remove('maths')
print("list now : ", list1)
# use print(x) not print (x)
# soz was just copied and paste
# at least fix it then :p
# zzzzz

a = [1, 2, 3, 4, 5, None, None, None]
a.remove(None)

print(a)

b = []
for i in a:
    if i is not None:
        b.append(i)
print(b)
c = [i for i in a if i is not None]
print(c)

# literally just thought of method b!
# but c is cool!

# c is slightly better, it's called a list comprehension
# but b is perfectly fine for now
# if you couldn't tell, remove only removes it once
# and so to do it like that you'd need to remove, then check if you've
# removed them all
# and each remove step takes time n, and each check does too
# so that's probably quadratic
# but b/c takes about time n on its own
# so better

# yeah eventually got why remove wasn't working
# but cool yeah i like how c works
