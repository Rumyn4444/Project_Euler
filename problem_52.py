def has_same_digits(x, y):
    return sorted(str(x)) == sorted(str(y))
x = 100000
while True:
    if all(has_same_digits(x, x * i) for i in range(2, 7)):
         print(x)
         break
    x += 1


# Solution 2
def same_digits(x):
    s1 = sorted(str(x))
    s2 = sorted(str(2*x))
    s3 = sorted(str(3*x))
    s4 = sorted(str(4*x))
    s5 = sorted(str(5*x))
    s6 = sorted(str(6*x))
    return s1 == s2 == s3 == s4 == s5 == s6
x = 1
while not same_digits(x):
    x += 1
print(x)
