class student():
     def __init__(self,name,roll,college):
        self.name=name
        self.roll=roll
        self.college=college
     def display(self):
        print(self.name,self.roll, self.college)
        
     @classmethod
     xdef sample(cls):
        cls.college='AEC'
        print(cls.college)   
            
    
            

a=student('Prachi Ranjan', 5,'ACET')
a.display()
a.sample()

b=student('Vishakha Vishwash', 54,'ACOE')
b.display()
b.sample()

c=student('Tanya Sambhawi', 34,'AEC')
c.display()
c.sample()
