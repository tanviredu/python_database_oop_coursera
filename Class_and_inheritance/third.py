#### we understand the class attribute and 
#### the instance attribute
#### there are two type of attribute
#### 1) class atribute
#### 2) instance attribute

## making a class
class Employee:

    ### this is a class attribute
    numberOfWorkingHours = 40


## now instantiate the class
employeeOne = Employee()
employeeTwo = Employee()

print(employeeOne.numberOfWorkingHours)
print(employeeTwo.numberOfWorkingHours)

## we can access the class variable with this
## and when we create an object
## all the object will have ths attribute



### now we can add attribute directly but it depend on the 
### object and only this object can have it

employeeOne.name = "tanvir"

print(employeeOne.name)

### this will show an error
#print(employeeTwo.name)

### this is the instance attribute


employeeTwo.name = "ornob"
print(employeeTwo.name)