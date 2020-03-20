#### lets make a class with the 
#### @property
class Celsius:
    
    def __init__(self,tmp = 0):
        self.tmp = tmp

    def convert_to_farenhite(self):
        return (self.tmp * 1.8) + 32


### lets tun it
m = Celsius()
m.tmp = 100
print(m.tmp)
print(m.convert_to_farenhite())
print(m.tmp)
print(m.__dict__)


### the problem in this class is you can use any value 
## in htis and it just convert it
## what happen if you want to put this in a limit
## like you can excede the limite of an input
## lets see it
