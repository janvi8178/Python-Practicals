# Name: Janvi
# Roll Number: 26570025

# Practical 12: Define a class Employee that stores information about employees in the company.
# Data members : count (number of objects created) and, for every employee, an employee number,
#                Name, Dept, Basic, DA and HRA.
# Function members:
#   a. __init__ to initialize and/or update the members; the program is terminated if any of
#      Basic, DA and HRA is set to a negative value
#   b. salary, which returns Basic + DA + HRA
#   c. __del__ to decrease the number of objects created for the class
#   d. __str__ to display the details of an employee along with the salary in a proper format
import sys


class Employee:
    count = 0                                   # class attribute: number of live Employee objects

    def __init__(self, emp_no, name, dept, basic, da, hra):
        self._counted = False
        self.emp_no = emp_no
        self.name = name
        self.dept = dept
        self.update(basic, da, hra)             # validates Basic, DA and HRA
        Employee.count += 1                     # reached only if the values were valid
        self._counted = True

    def update(self, basic, da, hra):
        """Set (or change) Basic, DA and HRA. A negative value terminates the program."""
        if basic < 0 or da < 0 or hra < 0:
            print("Error: Basic, DA and HRA cannot be negative. Terminating the program.")
            sys.exit(1)
        self.basic = basic
        self.da = da
        self.hra = hra

    def salary(self):
        return self.basic + self.da + self.hra

    def __del__(self):
        if getattr(self, "_counted", False):    # an object that failed validation was never counted
            Employee.count -= 1

    def __str__(self):
        return (f"Employee No : {self.emp_no}\n"
                f"Name        : {self.name}\n"
                f"Department  : {self.dept}\n"
                f"Basic       : Rs. {self.basic:,.2f}\n"
                f"DA          : Rs. {self.da:,.2f}\n"
                f"HRA         : Rs. {self.hra:,.2f}\n"
                f"Salary      : Rs. {self.salary():,.2f}")


e1 = Employee(101, "Janvi", "Computer Science", 30000, 12000, 8000)
e2 = Employee(102, "Aman Verma", "Mathematics", 28000, 11000, 7500)
e3 = Employee(103, "Neha Singh", "Physics", 32000, 12500, 8500)

print(e1)
print("-" * 40)
print(e2)
print("-" * 40)
print(e3)
print("-" * 40)
print("Employees created:", Employee.count)

del e3                                          # object destroyed -> __del__ runs
print("After deleting one employee:", Employee.count)

e1.update(35000, 14000, 9000)                   # update the pay components of e1
print("\nAfter updating e1:")
print(e1)

print("\nTrying to create an employee with a negative DA ...")
e4 = Employee(104, "Test User", "Chemistry", 25000, -500, 7000)
print("This line is never reached.")
