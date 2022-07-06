import json

with open("blogs.json")as f:
    data=json.load(f)
print(len(data))