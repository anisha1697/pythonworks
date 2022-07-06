from Media.models import users
session{}


def authentificate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return(user)
# print(authentificate(username="nikil",password="Password@123"))
def Loginview(*args,**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")



