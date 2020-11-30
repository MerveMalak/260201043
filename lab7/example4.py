employees = {}
for i in range(5):
  name = input("Employee name: ")
  salary = int(input("Employee salary: "))
  employees[name] = salary
salary_list = list(employees.values())
salary_list = sorted(salary_list,reverse= True)
max_salary = salary_list[:3] 
for i in max_salary:
  for current_key,current_value in employees.items():
    if current_value == i:
      print(current_key,current_value)
