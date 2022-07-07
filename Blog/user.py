import json
import random
with open("user.json")  as f:
    data=json.load(f)
    # print(data)
    all_user=[user["id"] for user in data]
    my_following=[user["followers"] for user in data if user["username"]=="akhil"][0]
    my_id = [user["id"] for user in data if user["username"] == "akhil"][0]
    # print(all_user)
    # print(my_following)
    to_follow=set(all_user)-set(my_following)
    to_follow.remove(my_id)
    print(to_follow)
    suggestion=random.sample([*to_follow],2)
    print(suggestion)
lst=[10,11,12,13]
st={*lst}
print(st)
