# class student:
#     def set_student(self,name,rollno,course):
#         #initializing instance variable-constructor
#         self.name=name
#         self.rollno=rollno
#         self.course=course
#     def print_student(self):
#         print(self.name,self.rollno,self.course)
# s1=student()
# s2=student()
# s1.set_student("anisha",24,"python")
# s1.print_student()
# s2.set_student("abisha",28,"cs")
# s2.print_student()
# class student:
#     def __init__(self,name,rollno,course):
#         self.name=name
#         self.rollno=rollno
#         self.course=course
#     def print_student(self):
#         print(self.name,self.rollno,self.course)
# s1=student("anisha",24,"python")
# s2=student("abisha",28,"cs")
# s1.print_student()
# s2.print_student()
class course:
    def __init__(self,course_id,course_name,course_fee):
        self.course_id=course_id
        self.course_name=course_name
        self.course_fee=course_fee
    def print_course(self):
        print(self.course_id,self.course_name,self.course_fee)
c1=course(1110,"python",30000)
c1.print_course()

