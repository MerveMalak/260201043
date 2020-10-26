number_of_lecture = int(input("Number Of Lecture: "))
gpa = float(input("GPA: "))

if number_of_lecture < 47:
  if gpa < 2 :
    print("Not enough number of lectures and GPA.")
  else:
    print("Not enough number of lectures.")
else:
  if gpa < 2 :
    print("Not enough GPA.")
  else:
    print("GRADUATED!")