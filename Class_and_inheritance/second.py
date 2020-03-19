class Employee:
    ''' this is the class Description'''
    name = "Ben"
    designation = "Sales Executive"
    salesMadeThisWeek = 6

    def hasAchivedTarget(self):
        if self.salesMadeThisWeek >=5:
            print("Target has been achived")
        else:
            print("Target is not achived")



#help(Employee)  ### this helps to see the description with doc string

employee = Employee() ## creating the object
print(employee.name)
employee.hasAchivedTarget()
employee2 = Employee()
print(employee2.name)
employee2.hasAchivedTarget() 