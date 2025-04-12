# Polymorphism
# Polymorphism is the ability of different objects to respond to the same method call in different ways.
# In Python, polymorphism is achieved through method overriding and operator overloading.
# Method overriding is when a derived class provides its own implementation of a method that is already defined in its base class.
# Operator overloading is when we define the behavior of operators for user-defined classes.
# In this example, we will demonstrate polymorphism using method overriding and operator overloading.
# We will create a base class Shape and two derived classes Circle and Rectangle.
# The base class Shape will have a method area() that will be overridden in the derived classes.
# The derived classes will also have their own implementation of the __str__() method to provide a string representation of the object.
# The __str__() method is called when we use the print() function on an object of the class.
# The derived classes will also implement the __add__() method to demonstrate operator overloading.
# The __add__() method is called when we use the + operator on two objects of the class.
# The __add__() method will return a new object that is the sum of the two objects.