class Employee:
    increment_percent = 1.05
    number_of_employess = 0

    def __init__(self, first, last, pay) -> None:
      self.fname = first
      self.lname = last
      self.pay = pay

      Employee.number_of_employess += 1

    def display_fullname(self):
      print(f"{self.fname} {self.lname}")
    
    def apply_incerement(self):
      self.pay = int(self.pay * self.increment_percent)

print('Num of employess', Employee.number_of_employess)
emp1 = Employee('xyz', 'abc', 100)
emp2 = Employee('pqr', 'abc', 120)
print('Num of employess', Employee.number_of_employess)

emp1.display_fullname()

print(emp1.pay)
emp1.apply_incerement()
print(emp1.pay)


emp1.increment_percent = 1.12
emp1.apply_incerement()
print(emp1.pay)
# for all
Employee.increment_percent = 1.20 
emp1.apply_incerement()
print(emp1.pay)

