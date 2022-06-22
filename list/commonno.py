lst1=[10,11,12,13,14]
lst2=[11,12,19,20,21]
duplicate_last=[]
for num in lst1:
    if num in lst2:
        duplicate_last.append(num)
        print(duplicate_last)
