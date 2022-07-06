students=open("students.txt")
all_students=[stud.rstrip("\n") for stud in students]
fail=open("failed.txt")
failed_students=[f.rstrip("\n")for f in fail]
passed=open("passed.txt","w")
passed_students=set(all_students)-set(failed_students)
print(passed_students)
for st in passed_students:
    passed.write(st)
add=open("passed.txt","a")
name="noor"
add.write(name)

