def compute():
    p = 1000
    for a in range(1, p + 1):
        for b in range(a + 1, p + 1):
            c = p - a - b
            if a * a + b * b == c * c:
                return str(a * b * c)
print(compute())
