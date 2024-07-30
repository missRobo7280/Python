##class Car():
##    def __init__(self):
##        print('hi')
##    def display(self):
##        print(10)
##        
##a=Car()
##a.display()
##
##b=Car()
##b.display()
class Car():
    country='India'#class variable
    def __init__(self,name,model):):#self is nothing but object(here a and b) and name and model are the parameters
        self.name=name#self,name and model are the instance variables here
        self.model=model
    def display(self):
        print(self.name,self.model)

a=Car('Kia',1234)
a.display()

b=Car('Maruti',5678)
b.display()
