#### lets make a class with the 
#### @property
####
class Celsius:
    
    def __init__(self,tmp = 0):
        self.set_tmp(tmp)

    def convert_to_farenhite(self):
        return (self.tmp * 1.8) + 32

    ## new

    def get_tmp(self):
        return self.tmp

    def set_tmp(self,value):
        if value < 273.0 *(-1):
            raise ValueError("You can not use under -273")
        self.tmp = value


### lets tun it
m = Celsius(-277)
m.tmp = float(input(">"))
print(m.tmp)
print(m.convert_to_farenhite())
print(m.tmp)
print(m.__dict__)



### now you can do it with less effort
