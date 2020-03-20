### what is a self parameter
### and why we use it
### what it is used for




### ans when you invoke a method of a object
### what python does is is this
### it invoke it in this stule
### class.method(instalce_object)
### thats exactly the reason tou need to have  a placeholder 
### in your method that in python we call it self
### you can use anything you want
### in tradition is useing the self keyword

class Employee():

    ## create a mehod
    def employeeDetails(self):
        self.name = "tanvir"
        age = 30
        print(self.name)
        print (age)


    ## lets create another method

    def printEmployeeDetails(self):
        print(self.name)  ## this  will print
        print(age)        ## this will create an error because
                          ## we dont use self in this in previouse function
                          ## so ies scpope in only the its ethod
        




employee = Employee()
employee.employeeDetails()
## if you want that your attribute be accessabile
## though out the  method
employee.printEmployeeDetails()
