def add_nums(**kwargs):
    print(sum([v for k,v in kwargs.items()]))
add_nums(n1=10,n2=20,n3=30)