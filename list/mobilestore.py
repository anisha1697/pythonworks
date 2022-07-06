mobiles=[
    [1000,"samsungA52","4g","AMOLED",27000,"samsung",12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung",20],
    [1002, "redminote10", "4g", "led", 17000, "redmi",50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi",70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung",1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung",34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung",7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung",89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung",0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple",0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus",67]

]
# print(f"total no of mobiles {len(mobiles)}")
# # total no of out of stock mobiles:
# out_of_stock=[mob for mob in mobiles if mob[-1]==0]
# print(out_of_stock)
#
# total_out_stock=[mob for mob in mobiles if mob[-1]==0]
# print(len(total_out_stock))
#
# avb_stock=[mob[-1] for mob in mobiles]
# print(sum(avb_stock))
#
# range=[mob for mob in mobiles if mob[4] in range(20000,30000)]
# print(range)
#
# fiveg_phones=[mob for mob in mobiles if mob[2]=="5g"]
# print(fiveg_phones)
#
# sam_phone=[mob for mob in mobiles if mob[-2]=="samsung"]
# print(sam_phone)
#
# max_price_phone=max([mob[4] for mob in mobiles])
# costly_price=[mob for mob in mobiles if mob[4]==max_price_phone]
# print(costly_price)
#
# min_price_phone=min([mob[4] for mob in mobiles])
# low_price=[mob for mob in mobiles if mob[4]==min_price_phone]
# print(low_price)
#
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
# print(mobiles)
#
# print(max(mobiles,key=lambda mob:mob[4]))
#
# print(min(mobiles,key=lambda mob:mob[4]))

