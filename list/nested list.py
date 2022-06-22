lst=[
    [10,11],
    [13,45],
    [50,16],
    [60,70]
 ]
flatten_list=[num for slist in lst for num in slist]
print(flatten_list)
num_gt_sixt=[num for num in flatten_list if num>16]
print(num_gt_sixt)
num_odd=[num for num in flatten_list if num%2!=0]
print(num_odd)

num_even=sum([num for num in flatten_list if num%2==0])
print(num_even)

flatten_list=[num for slist in lst for num in slist]
maped_list=[num+1 if num>25 else num-1 for num in flatten_list]
print(maped_list)
