def count_solutions(p):
    count = 0
    for a in range(1, p//3):
        for b in range(a, (p-a)//2):
            c = p - a - b
            if a**2 + b**2 == c**2:
                count += 1
    return count
max_count = 0
max_p = 0
for p in range(1, 1001):
    count = count_solutions(p)
    if count > max_count:
        max_count = count
        max_p = p

print("The maximum number of solutions of ({}) is reached when p = {}".format(max_count, max_p))
