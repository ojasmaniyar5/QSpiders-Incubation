#Single Inheritance Concepts.
class Father:
    property1 = "Car"
    property2 = "House"
    property3 = "Land"
    property4 = "Money"
    property5 = "Phone"
    
    @classmethod
    def display(cls):
        print(cls.property1,cls.property2, cls.property3, cls.property4, cls.property5)
    
class Child(Father):
    property1 = "Laptop"
    property2 = "Phone"
    property3 = "Watch"
    property4 = "Airpods"
    
    @classmethod
    def dis(cls):
        print(cls.property1,cls.property2, cls.property3, cls.property4)

obj = Child()
obj.dis()