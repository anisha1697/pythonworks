car={"name":"swift","brand":"maruti","price":"8lac","color":"red","fuel":"petrol","airbag":1}
print(car["brand"])
print(car["fuel"])
print("break_type" in car)
car["break_type"]="abs"
print(car)
car["airbag"]=2
print(car)