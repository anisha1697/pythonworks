class Course():
    course_name:str
    active_status:bool
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.active_status=kwargs.get("active_status")
    def __str__(self):
        return self.course_name
class Batch():
    course:Course
    batch_code:str
    batch_date:str

    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.batch_date=kwargs.get("batch_date")
    def __str__(self):
        return self.batch_code
class Student():
    student_name:str
    gender:str
    roll:str
    batch:Batch
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.gender=kwargs.get("gender")
        self.roll = kwargs.get("roll")
        self.batch = kwargs.get("batch")
    def __str__(self):
        return self.student_name

django=Course()
django.add_course(course_name="django",active_status="True")
bigdata=Course()
bigdata.add_course(course_name="bigdata",active_status="True")
print(django)
print(bigdata)
db1=Batch()
db1.add_batch(course=django,batch_code="djmay2k22",batch_date="5-5-2022")
bdb1=Batch()
bdb1.add_batch(course=bigdata,batch_code="dbmay2k22",batch_date="6-5-2022")
print(db1)
print(bdb1)
akshay=Student()
akshay.add_student(student_name="akshay",gender="male",roll="123",batch=db1)
nic=Student()
nic.add_student(student_name="nic",gender="male",roll="122",batch=db1)
joji=Student()
joji.add_student(student_name="joji",gender="male",roll="121",batch=bdb1)
print(akshay)
print(nic.batch.course)
