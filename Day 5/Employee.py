class Employee:
    count = 0
    def __init__(self):
        self.empName = "NA"
        self.empAge = 0
        self.salary = 0
        Employee.count += 1
        print Employee.count," Employee created"

    def getEmployeeDetails(self):
        print "Employee Name\t: ",self.empName
        print "Employee Age\t: ",self.empAge
        print "Employee Salary\t: ",self.salary
        
    def setEmployeeDetails(self,empName,empAge,salary):
        self.empName = empName
        self.empAge = empAge
        self.salary = salary


print "--------------------------------------------------"
emp1 = Employee()
emp1.setEmployeeDetails("Jhutan",25,50000)
emp1.getEmployeeDetails()
print "--------------------------------------------------"
emp2 = Employee()
emp2.setEmployeeDetails("Saddam",25,30000)
emp2.getEmployeeDetails()
print "--------------------------------------------------"
emp3 = Employee()
#emp2.setEmployeeDetails("Saddam",25,30000)
emp3.getEmployeeDetails()
print "--------------------------------------------------"
