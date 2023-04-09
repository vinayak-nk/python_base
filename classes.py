class Employee:
    def __init__(self, first, last) -> None:
      self.fname = first
      self.lname = last

    def display_fullname(self):
      print(f"{self.fname} {self.lname}")

emp1 = Employee('xyz', 'abc')
emp2 = Employee('pqr', 'abc')

emp1.display_fullname()
emp2.display_fullname()
Employee.display_fullname(emp1)