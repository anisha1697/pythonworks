import json

with open("countries.json",encoding="utf-8") as f:
    data=json.load(f)
print(len(data))


def get_country_data(country_name):
    return [country for country in data if country["name"].lower().startswith(country_name)]

country_lang=[country["languages"] for country in data if country['name']=="Ukraine"]
print(country_lang)

currency_det=[country["currencies"] for country in data if country["name"].startswith("Palestine")]
print(currency_det)

currency_detail=[country["currencies"] for country in data if country["name"].lower().startswith("sri")]
currency_name=[details.get("name")for details in currency_detail[0]]
print(currency_name)

aus_data=get_country_data("austria")
print(aus_data[0].get("borders"))

india_data=get_country_data("india")
print(india_data[0].get("borders"))
country_border=india_data[0].get("borders")

neighbouring=[country.get("name") for country in data if country["alpha3Code"] in country_border]
print(neighbouring)

maximum_pop=max(data,key=lambda d:d.get("population"))
print(maximum_pop["name"])
minimum_pop=min(data,key=lambda d:d.get("population"))
print(minimum_pop["name"])


