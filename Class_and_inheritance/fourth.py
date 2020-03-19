### the instance that you create
### if you want to add the method
### you need to pass the instance variable
### first in the first positional argument


# class Employee:
    
#     def employeeDetails(employee):
#         ## this is the instance variabel
#         ## that you need to pass
#         ## but we will do other things
#         ## insted of envoking this
#         print("hello")

# employee = Employee()
# employee.employeeDetails()



## insted we apply the self parameter

class Employee:
    def employeeDetails(self):
        self.name = "Tanvir Rahman"
        print ("Name is {} ".format(self.name))


employee = Employee()
employee.employeeDetails()
