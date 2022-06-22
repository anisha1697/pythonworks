def chk_prime(num):
    if num>1:
        for i in range(2,int(num+1)):
            if (num+1)%2==0:
                print(chk_prime(10))

