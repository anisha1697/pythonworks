fmob=open("mobile.txt")
all_mobile=[mobiles.rstrip("\n").split(",")for mobiles in fmob]
# for m in fmob:
#     mobile=m.rstrip("\n").split(",")
#     all_mobile.append(mobile)
# print(all_mobile)
costly_mobile=max(all_mobile,key=lambda mob:int(mob[1]))
print(costly_mobile)
five_g=[mob for mob in all_mobile if mob[3]=="5g"]
print(five_g)
