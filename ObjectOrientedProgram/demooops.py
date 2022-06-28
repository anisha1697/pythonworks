# class parent:
#     def phone (self):
#         print("nokia,oneplus")
#     def bike (self):
#          print("activa")
# class child(parent):
#     pass
# c1=child()
# c1.phone()
# c1.bike()
#multilevel inheritence

# class p1:
#     def m1(self):
#         print("inside m1")
# class p2:
#     def m2(self):
#         print("inside m2")
# class p3(p2,p1):
#     def m3(self):
#         print("inside m3")
# p3=p3()
# p3.m3()
# p3.m2()
# p3.m1()
#overriding method

class parent:
  def phone (self):
        print("nokia,oneplus")
  def bike (self):
         print("activa")
class child(parent):
  def phone(self):
      print("iphone")
  def bike(self):
      print("duke")
c1=child()
c1.phone()
c1.bike()
