

student_marks= {'Abi':85, 'Bala': 89, 'Chandru': 75, 'Deepak': 84 }
Student_name= input("Enter the Student's Name:")
print(student_marks.get(Student_name,"Student Not Found"))

a=[1,2,3,4,5,6,7,8,9,10]
g=[]
g= a[0:5]
print(list(g))
h=g.copy()
h.reverse()
print(list(h))