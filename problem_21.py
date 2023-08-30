def suma_del(n):
    s = 0
    for i in range (1, int(n/2+1)):
        if n%i == 0:
            s += i
    return s
sum_drug = 0
for i in range (2, 10000):
    j = suma_del(i)
    if i != j and i == suma_del(j):
        sum_drug += i + j
print (sum_drug) 
