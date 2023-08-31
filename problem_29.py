list_end = []    
for a in range (2, 101):
    for b in range (2, 101):
        chlen = a**b
        if chlen not in list_end:
            list_end.append(chlen)
print (len(list_end))
