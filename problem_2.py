def Sum_Even_Fibonacci(n):
    s1, s2, s = 0, 1, 0
    while s2 < n:
        s1, s2 = s2, s1+s2
        if s2 % 2 == 0:
            s += s2
    return s
print(Sum_Even_Fibonacci(4000000))
