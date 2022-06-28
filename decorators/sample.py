def smart_sub(fun):

    def wrapper(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fun(n1,n2)
    return wrapper

@smart_sub
def sub(n1,n2):
    return n1-n2
@smart_sub
def div(n1,n2):
    return n1/n2

print(div(10,20))
print(sub(30,20))




