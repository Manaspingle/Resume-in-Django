# Base Class
class Developer:
    def getDetails(self):
        self.name = input("Enter Name: ")
        self.id = input("Enter ID: ")
        self.department = input("Enter Department: ")
        self.designation = input("Enter Designation: ")
        self.basicSalary = float(input("Enter Basic Salary: "))

    def displayDetails(self):
        print("\n--- Developer Details ---")
        print("Name        :", self.name)
        print("ID          :", self.id)
        print("Department  :", self.department)
        print("Designation :", self.designation)
        print("Basic Salary:", self.basicSalary)


# Derived Class
class Components(Developer):
    def displaySalComponents(self):
        self.hra = 0.40 * self.basicSalary
        self.ta = 0.30 * self.basicSalary
        self.da = 0.20 * self.basicSalary
        self.pfDed = 2300

        print("\n--- Salary Components ---")
        print("HRA (40%)   :", self.hra)
        print("TA (30%)    :", self.ta)
        print("DA (20%)    :", self.da)
        print("PF Deduction:", self.pfDed)


# Derived Class
class Salary(Components):
    def calculateSal(self):
        self.grossSalary = self.basicSalary + self.hra + self.ta + self.da
        self.netSalary = self.grossSalary - self.pfDed

    def displaySal(self):
        print("\n--- Salary Details ---")
        print("Gross Salary:", self.grossSalary)
        print("Net Salary  :", self.netSalary)


# Main Program
obj = Salary()

obj.getDetails()
obj.displayDetails()
obj.displaySalComponents()
obj.calculateSal()
obj.displaySal()