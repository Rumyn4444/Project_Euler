list_pan = []
for a in range (1, 10000):
    for b in range (1, 100):
        c = a*b
        if c not in list_pan and sorted(str(a)+str(b)+str(c)) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            list_pan.append(c)

print (sum(list_pan))
