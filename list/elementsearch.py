arr=[10,11,12,13,14,15,16,17]
element=17
flag=0
arr.sort()
low=0
upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2
    if element==arr[mid]:
        flag=1
        break
    elif  element>mid:
        low=mid+1
    elif element<mid:
        upp=low-1
print("found" if flag>0 else "not found")