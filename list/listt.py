names=["c++","c","jaava","python","script"]
for i in range(0,len(names)):
    print(names[i])

numbers=[13,14,15,16,17,18]
for num in numbers:
 if num%2==0:
    print(num)

numbers=[13,14,15,16,17,18]
count=0
for num in numbers:
    if num in range(14,19):
        count+=1
    print(count)

numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
p_count=0
n_count=0
z_count=0
for n in numbers:
    if n>0:
        p_count+=1
    elif n<0:
        n_count+=1
    elif n==0:
        z_count+=1
print(f"+ve {p_count} -ve {n_count} zero {z_count}")
numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
sum=0
for n in numbers:
    sum+=n
print(sum)
numbers=[-1,2,0,3,4,5,-2,0,3,4,-5,0,7,0]
p_sum=0
n_sum=0
z_sum=0
for n in numbers:
    if n>0:
        p_sum+=n
    elif n<0:
        n_sum+=n
    elif n==0:
        z_sum+=n
print(f"+ve sum nos{p_sum} -ve sum nos {n_sum} zero nos {z_sum}")

print(dir(list))


