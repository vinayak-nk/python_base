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

    @classmethod
    def set_increment_amount(cls, amount):
      cls.increment_percent = amount

    # Alternative constructor method
    @classmethod
    def from_string(cls, emp_str):
      fname, lname, pay = emp_str.split('-')
      return cls(fname, lname, pay)
    
    #staticmethod
    @staticmethod
    def is_work_day(day): #it does not take either instance or class as arg
      if day.weekday() == 5 or day.weekday() == 6:
        return False
      return True

emp1 = Employee('xyz', 'abc', 100)
emp2 = Employee('pqr', 'abc', 100)

new_emp = Employee.from_string('vinayak-k-123')
print('from string', new_emp.display_fullname())

print(emp1.pay)
emp1.apply_incerement()
print(emp1.pay)

print(emp2.pay)
Employee.set_increment_amount(1.10)
emp2.apply_incerement()
print(emp2.pay)

import datetime
my_date = datetime.date(2023, 4, 10)
print(Employee.is_work_day(my_date))