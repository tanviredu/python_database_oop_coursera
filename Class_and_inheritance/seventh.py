##  what happend 
##  if your method in the class
## does a basic job and dont need the self parameter
## thats called static method
## lets see how to do that
## in python the static method is called a decorator
## decorator are function that takes another function
## and  extends theri functionality 
## it starts with @staticmethod
## it takes another function and extend their functionality
## and ignore the binding of the object
## just easy to remember you dont need to use "self" in the static method

class Employee:
    def employeeDetails(self):
        self.name = "tanvir"

    @staticmethod
    def welcome():
        print("Welcome to the organization")


employee = Employee()
employee.employeeDetails()
employee.welcome()
