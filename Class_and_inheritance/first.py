
### this is how to define the class
#### and instantiate the class

class Employee:
    ## define the attribute of the class
    name = "Ben"

    ## this is a method

    def changeName(self):
        Employee.name = "Mark"



## create an employee object
employee = Employee()
print(employee.name)
## apply the method
employee.changeName()  ## this is the function 
## after the change lets see the name again
print(employee.name)

print(employee)


### you can do this in another way
### lets see 

class Employee2:
    name = "ben"

    def changeName(self):
        self.name = "Mark"


## create an employee object
employee = Employee2()
print(employee.name)
## apply the method
employee.changeName()  ## this is the function 
## after the change lets see the name again
print(employee.name)

print(employee)


## if you use the self 
## you dont have to change the attribute
## using self will change the class attribute 

    