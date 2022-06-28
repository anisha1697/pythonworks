class Emp(object):
    def __init__(self,**kwargs):
        self.id=kwargs.get(id)
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")
    def __str__(self):
        return self.role
class Dept():
    def __init__(self,**kwargs):
        emp=kwargs.get("emp")
        if emp.role=="hr":
            self.dept_name=kwargs.get("dept_name")
            self.emp=kwargs.get("emp")
        else:
            print("no access")
    def __str__(self):
        return self.dept_name
employee=Emp(id=100,name="ram",role="hr")
print(employee)
dep=Dept(dept_name="cs",emp=employee)
print(dep)
