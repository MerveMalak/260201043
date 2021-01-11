class Employee:
  def __init__(self,name,salary):
    self.name = name
    self.salary = salary

  def get_name(self):
    return self.name
  
  def set_name(self,name):
    self.name = name
    
  def get_salary(self):
    return self.salary

  def set_salary(self,salary):
    if salary > 0:
      self.salary = salary

  def display(self):
    print("Name: {}, salary: {}".format(self.name,self.salary))

class Company:
  def __init__(self):
    self.employee_list = []
  
  def get_employye_list(self):
    return self.employee_list

  def set_emplooye_list(self,employee_list):
    if isinstance(employee_list,list):
      self.employee_list = employee_list

  def add_employee(self,new_employee):
    if isinstance(new_employee,Employee):
      self.employee_list.append(new_employee)

  def average_salary(self):
    total_salary = 0
    for emp in self.employee_list:
      total_salary += emp.get_salary()
    return total_salary / len(self.employee_list)

  def display_employees(self):
    for emp in self.employee_list:
      emp.display()

e1 = Employee("e1", 2550)
e2 = Employee("e2", 5000)
e3 = Employee("e3", 6000)
company = Company()
company.add_employee(e1)
company.add_employee(e2)
company.add_employee(e3)
print(company.average_salary())
company.display_employees()
e4 = Employee("e4",5600)
company.add_employee(e4)
print(company.average_salary())
company.display_employees()