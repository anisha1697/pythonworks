lst=[10,11,12,13,14,15,16,17,12,12,12,12,100]
oddlst=[]
for num in lst:
    if num%2!=0:
        oddlst.append(num)
print(oddlst)
oddlst.sort(reverse=True)
print(oddlst)
evenlst=[]
for num in lst:
    if num%2==0:
        evenlst.append(num)
print(evenlst)
oddlst=[num for num in lst if num%2!=0]
print(oddlst)
print(lst.count(12))