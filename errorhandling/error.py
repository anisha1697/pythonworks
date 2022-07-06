

#
#
# num1=int(input("enter no 1"))
#
# num2=int(input("enter no 2"))
# try:
#     res=num1/num2
#     print(f"res {res}")
# except Exception as e:
#     print(e)
#
# print("data base")
# print("file operation")
#
# num1=int(input("enter no 1"))
# num2=int(input("enter no 2"))
# try:
#     print(num1/num2)
# except Exception as e:
#     num2=int(input("enter no 2"))
#     print(num1/num2)
#
# finally:
#     print("file1")
#     print("file 2")

# # custom error
# age=int(input("enter no 1"))
#
# if age<18:
#     raise Exception("not eligible for voting")
# else:
#     print("eligible")
#
phone_no=len(input("enter phone no"))

if phone_no!=10:
    raise Exception("invalid phone no")
else:
    print("valid")
#try:
# doutful code
# except: handling code
# finally: clean up process
# raise key throwing custom exception

