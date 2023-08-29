maximum = 0
for i in range (999, 99, -1):
    for j in range (999, 99, -1):
        result = i*j
        if str(result) == str(result)[::-1] and result > maximum:
            maximum = result
print (maximum)
