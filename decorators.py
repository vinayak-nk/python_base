class Employee:
  def __init__(self, fname, lname, salary) -> None:
    self.fname = fname
    self.lname = lname
    self.salary = salary
    # self.email = f"{fname}.{lname}@email.com"

  @property
  def email(self):
    return f"{self.fname}.{self.lname}@email.com"

  @property
  def fullname(self):
    print(f"{self.fname} {self.lname}")
  
  @fullname.setter
  def fullname(self, name):
    fname, lname = name.split(' ')
    self.fname = fname
    self.lname = lname

  @fullname.deleter
  def fullname(self):
    self.fname = None
    self.lname = None

dev1 = Employee('vin', 'k', 110)

dev1.fname = 'vinay'

print(dev1.fname) # vk
print(dev1.email) # Dev.abc@email.com
dev1.fullname # vk abc

dev1.fullname = 'vinayak k'
dev1.fullname

del dev1.fullname
dev1.fullname