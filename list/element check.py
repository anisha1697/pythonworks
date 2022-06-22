lst=[10,11,12,13,14,15,16,17]
lst.sort()
element=210
flag=0
for num in lst:
    if element==num:
        flag=1
        break
print("element found " if flag!=0 else "not found")
lst=[10,11,12,13,14,15,16,17]
element=11
flag=0
for i in range(0,len(lst)):
    if element==lst[i]:
        flag=1
        break
print("element found " if flag != 0 else "not found")
lst.sort(reverse=True)
print(lst)
lst.remove(12)
print(lst)
lst.insert(0,1000)
print(lst)
