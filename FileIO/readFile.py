# f=open("abc.txt")
# for lines in f:
#     lst=[]
#     lst.append(lines)
#     print(lst)
out=[line.rstrip("/n")for line in f]
print(out)
# print(dir(str))

