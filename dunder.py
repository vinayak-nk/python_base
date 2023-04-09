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

  def __repr__(self) -> str:
    return f"Employee {self.fname}, {self.lname}, {self.salary}"

  def __str__(self) -> str:
    return "Employee {}".format(self.email)


dev1 = Employee('Dev', 'abc', 110)
dev2 = Employee('Tester', 'xyz', 120)

print(dev1)
print(repr(dev2))
print(dev1.__repr__())
print(str(dev1))