# Inheritance Concepts
# This is a multilevel inheritance example in Python.
# Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called the child or derived class) to inherit attributes and methods from another class (called the parent or base class). This promotes code reusability and establishes a hierarchical relationship between classes.
# Inheritance can be single, multiple, or multilevel. In this example, we will focus on multilevel inheritance, where a class inherits from another derived class.
# Multilevel inheritance is a type of inheritance where a class is derived from another derived class. This creates a chain of inheritance, allowing the derived class to inherit attributes and methods from both the base class and the intermediate derived class.
# This allows for a more organized and structured approach to code organization, as well as the ability to create more complex class hierarchies.
# This is the real world example of inheritance in Python.
class Bank:
    def __init__(self, name, phone, aadhar, address):
        self.name = name
        self.phone = phone
        self.aadhar = aadhar
        self.address = address
    def display(self):
        print(self.name, self.phone, self.aadhar, self.address)
        
class Up_Bank(Bank):
    def __init__(self, name, phone, aadhar, address, pan):
        super().__init__(name, phone, aadhar, address)
        self.pan = pan
    def display2(self):
        super().display()
        print(self.pan)
        
class Up_Bank_Pro(Up_Bank):
    def __init__(self, name, phone, aadhar, address, pan, kyc):
        super().__init__(name, phone, aadhar, address, pan)
        self.kyc = kyc
    def display3(self):
        super().display()
        print(self.kyc)
        
cust = Up_Bank_Pro('Ojas', '8010782571', '4001-2579-1346', 'PCMC,Pune', 'ABCDE1234F', 'Verified')
cust.display3()








# In this example, we have a base class Bank and two derived classes Up_Bank and Up_Bank_Pro.
# The base class Bank has four attributes: name, phone, aadhar, and address.
# The derived class Up_Bank has an additional attribute pan, and the derived class Up_Bank_Pro has an additional attribute kyc.
# The derived classes inherit the attributes and methods of the base class and can also have their own attributes and methods.
# The display method in the base class is used to display the attributes of the base class, and the display2 and display3 methods in the derived classes are used to display the attributes of the derived classes.
# The display3 method in the Up_Bank_Pro class calls the display method of the base class and then displays its own attribute kyc.
# The final object cust is created from the Up_Bank_Pro class, and the display3 method is called to display all the attributes of the object.