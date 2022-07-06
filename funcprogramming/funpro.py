lst=[10,1,2,51]
num_out=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(num_out)
squares=list(map(lambda n:n**2,lst))
print(squares)