def find_smallest_n():
    target_count = 100
    n = 2
    count = 0
    while count <= target_count:
        count = 0
        for y in range(n+1, 2*n):
            x = (n*y) / (y - n)
            if x.is_integer():
                count += 1    
        n += 1
    return n - 1

smallest_n = find_smallest_n()
print(smallest_n)
