grade_list = []
average_list = []
number = int(input("How many students?: "))
for i in range(number):
    student_grade = list(map(float,input("Enter student midterm1,midterm2,final grades(use a comma): ").split(",")))
    grade_list.append(student_grade)
for i in grade_list:
    average_grade = i[0]*(0.3) + i[1]*(0.3) + i[2]*(0.4)
    average_list.append(average_grade)
print(average_list)