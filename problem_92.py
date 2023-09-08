def get_next_number(n):
    return sum(int(digit)**2 for digit in str(n))

def ends_with_89(n):
    while n != 1 and n != 89:
        n = get_next_number(n)
    return n == 89

count_89 = 0
for n in range(1, 10000000):
    if ends_with_89(n):
        count_89 += 1
print(count_89)
