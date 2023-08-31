#Solution 1:
import math
answer = 1
for i in range(1, 21):
    answer *= int(i / math.gcd(i, answer))
print (answer)


#Solution 2:
# Function for finding the least common divisor of two numbers
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
# Function for finding the least common multiple of two numbers
def lcm(a, b):
    return a * b // gcd(a, b)
# Find the least common multiple of all numbers from 1 to 20
lcm_all = 1
for i in range(1, 21):
    lcm_all = lcm(lcm_all, i)
print(lcm_all)
