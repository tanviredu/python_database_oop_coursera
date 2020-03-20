## make a reverse class
## that will reverse the sequence
## ithe "__iter__" method is a interesting method
## that returns a object with a next() method
## so you can iterate this object


class Reverse:
    

    ## this is the constructor function
    def __init__(self,data):
        self.data = data
        self.index = len(data)


    ### make the object iterable
    ### so you can iterate this object
    def __iter__(self):
        return self
    
    ## this next
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index = self.index - 1
            ## decrease the index and get the data related to the index
            return self.data[self.index]


rev = Reverse("spam")
print(rev)

print(rev.__iter__())
print(rev.__next__())

#for item in rev:
#    print(item)

##  you an iterare this wil the for loop and also the next method
for item in range(10):
    print(rev.__next__())
