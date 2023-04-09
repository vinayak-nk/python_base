class Employee:
  NUMBER_OF_EMPLOYEES = 0
  INCREMENT = 1.05

  def __init__(self, fname, lname, salary) -> None:
    self.fname = fname
    self.lname = lname
    self.salary = salary
    self.email = f"{fname}.{lname}@email.com"

    Employee.NUMBER_OF_EMPLOYEES += 1
  
  def increment(self):
    self.salary = int(self.salary * self.INCREMENT)

class Developer(Employee):
  INCREMENT = 1.10

  def __init__(self, fname, lname, salary, prog_lang) -> None:
    super().__init__(fname, lname, salary)
    # Employee.__init__(self, fname, lname, salary)
    self.prog_lang = prog_lang

class Manager(Employee):
  INCREMENT = 1.20
  def __init__(self, fname, lname, salary, employees=None) -> None:
    super().__init__(fname, lname, salary)
    if employees is None:
      self.employees = []
    else:
      self.employees = employees
   
  def add_employees(self, emp):
    if emp not in self.employees:
      self.employees.append(emp)
  
  def remove_employees(self, emp):
    if emp in self.employees:
      self.employees.remove(emp)
  
  def list_employees(self):
    for emp in self.employees:
      print(f"--> {emp.email}")


dev1 = Developer('Dev', 'abc', 110, 'python')
dev2 = Developer('Tester', 'xyz', 120, 'java')

mgr = Manager('Manager', 'k', 150)
print(mgr.email)

mgr.list_employees()
mgr.add_employees(dev1)
mgr.add_employees(dev2)
mgr.list_employees()
mgr.remove_employees(dev1)
print('AFTER REMOVE')
mgr.list_employees()

