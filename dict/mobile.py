mobile={"mobile_name":"oneplus","ram":12,"price":39000,"band":"2g"}
print(mobile["mobile_name"])
print(mobile.get("ra"))
mobile["band"]="5g" if "band" in mobile else "4g"
print(mobile)
if mobile["price"]>40000:
    mobile["price"]-=1000
else:
    mobile["price"]-=500
print(mobile)

text= "hai hello hai hello"

