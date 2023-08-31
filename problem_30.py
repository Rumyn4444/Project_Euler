def sum_fifth():
    return sum(i for i in range(2, 1000000) if i == sum(int(c)**5 for c in str(i)))
    
print (sum_fifth())

