f=open("abc.txt","w")
lst=["python","java","c++"]
for lan in lst:
    lan+="\n"
    f.write(lan)