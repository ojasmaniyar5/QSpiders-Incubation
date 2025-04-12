class Grandfather:
    a = 'House'
    b = 'Car'
    c = 'Land'
    d = 'No_Job'
    e = 'Businessman'
    
    @classmethod
    def display(cls):
        print(cls.a, cls.b, cls.c)
        
class Father(Grandfather):
    a = 'Money'
    b = 'Phone'
    c = 'Bussinessman'
    
    
    @classmethod
    def display(cls):
        print(cls.a, cls.b, cls.c)
        
class Child(Father):
    f = 'Laptop'
    g = 'Watch'
    
    @classmethod
    def display(cls):
        print(cls.f, cls.g)
        
obj = Child()
obj.display()
print(obj.a)