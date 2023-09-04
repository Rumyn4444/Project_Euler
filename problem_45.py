def is_pentagonal(num):
    n = (1 + (1 + 24 * num) ** 0.5) / 6
    return n == int(n)

def is_hexagonal(num):
    n = (1 + (1 + 8 * num) ** 0.5) / 4
    return n == int(n)

n = 286
while True:
    triangle = n * (n + 1) // 2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print(triangle)
        break
    n += 1
