#Abstraction Concept
#Abstraction is a process of hiding the implementation details and showing only the functionality to the user.
#It helps to reduce complexity and increase efficiency.
#Abstraction can be achieved using abstract classes and interfaces.
#Abstract classes are classes that cannot be instantiated and are meant to be inherited by other classes.
#They can have abstract methods (methods without implementation) and concrete methods (methods with implementation).
#Abstract methods must be implemented by the subclasses.
#Interfaces are similar to abstract classes but can only have abstract methods.
#They are used to define a contract for the classes that implement them.
#In Python, we can use the abc module to create abstract classes and methods.
#The abc module provides the ABC class and the abstractmethod decorator to define abstract classes and methods.
#We can also use the ABCMeta metaclass to create abstract classes.
#Example usage:
from abc import ABC, abstractmethod
class Shape(ABC):  # Abstract class
    @abstractmethod
    def area(self):  # Abstract method
        pass

    @abstractmethod
    def perimeter(self):  # Abstract method
        pass
#In this example, the Shape class is an abstract class that has two abstract methods: area and perimeter.
#Any class that inherits from Shape must implement these methods.
#This allows us to define a common interface for all shapes without specifying how the area and perimeter are calculated.
#We can create concrete classes that inherit from Shape and implement the abstract methods.
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
    #In this example, the Circle class inherits from Shape and implements the area and perimeter methods.
#We can create an instance of Circle and call the area and perimeter methods.
circle = Circle(5)
print("Area of Circle:", circle.area())  # Area of Circle: 78.5
print("Perimeter of Circle:", circle.perimeter())  # Perimeter of Circle: 31.400000000000002
# #The above code demonstrates abstraction by defining a common interface for all shapes without specifying how the area and perimeter are calculated. This allows us to create different shapes that implement the same interface, making it easier to work with different types of shapes in a consistent way.
# #Abstraction is a powerful concept that allows us to create flexible and reusable code. By defining a common interface for different classes, we can create systems that are easy to understand and maintain. This allows us to build complex systems while keeping the code organized and manageable.
# #Abstraction is a key principle of object-oriented programming that helps to create robust and maintainable code. By abstracting away the implementation details, we can create objects that are easy to use and understand. This allows us to build complex systems while keeping the code organized and manageable.


#List down the key points of abstraction in Python:
#1. Abstraction is a process of hiding the implementation details and showing only the functionality to the user.
#2. It helps to reduce complexity and increase efficiency.
#3. Abstraction can be achieved using abstract classes and interfaces.
#4. Abstract classes are classes that cannot be instantiated and are meant to be inherited by other classes
#5. They can have abstract methods (methods without implementation) and concrete methods (methods with implementation
#6. Abstract methods must be implemented by the subclasses 
#7. Interfaces are similar to abstract classes but can only have abstract methods.
#8. They are used to define a contract for the classes that implement them.
#9. In Python, we can use the abc module to create abstract classes and methods.
#10. The abc module provides the ABC class and the abstractmethod decorator to define abstract classes and methods.
#11. We can also use the ABCMeta metaclass to create abstract classes.
#12. Abstraction allows us to define a common interface for different classes without specifying how the methods are implemented.
#13. This allows us to create flexible and reusable code.
#14. Abstraction is a key principle of object-oriented programming that helps to create robust and maintainable code.
#15. By abstracting away the implementation details, we can create objects that are easy to use and understand.

#Advantages of Abstraction:
#1. Simplifies complex systems by hiding unnecessary details.
#2. Promotes code reusability and maintainability.
#3. Enhances security by restricting access to implementation details.
#4. Improves performance by reducing the amount of code that needs to be executed.
#5. Facilitates easier testing and debugging by providing a clear and well-defined interface.
#6. Encourages a modular approach to software development, making it easier to manage and understand large codebases.
#7. Allows for easier collaboration among developers by providing a clear contract for how classes should interact with each other.

#Real World Example of Abstraction:
#1. A car is a good example of abstraction. The driver only needs to know how to operate the steering wheel, pedals, and gear shift. The complex mechanics of the engine, transmission, and other components are hidden from the driver.
#2. A smartphone is another example of abstraction. The user interacts with the touchscreen and apps, while the underlying hardware and software work together to provide the desired functionality.
#3. A bank ATM is another example of abstraction. The user interacts with the ATM interface to withdraw cash, check balance, etc., while the complex banking systems and processes are hidden from the user.
#4. A computer operating system is another example of abstraction. The user interacts with the graphical user interface (GUI) to perform tasks, while the underlying hardware and software work together to provide the desired functionality.
#5. A web browser is another example of abstraction. The user interacts with the browser interface to access websites, while the underlying network protocols and server interactions are hidden from the user.
#6. A video game console is another example of abstraction. The user interacts with the controller and game interface, while the complex graphics and processing are handled by the console's hardware and software.
#7. A smart home system is another example of abstraction. The user interacts with the smart home app to control devices, while the underlying hardware and software work together to provide the desired functionality.
#8. A cloud storage service is another example of abstraction. The user interacts with the web interface or app to upload and download files, while the underlying storage infrastructure and data management are hidden from the user.
#9. A social media platform is another example of abstraction. The user interacts with the app or website to post updates, share photos, and connect with friends, while the underlying algorithms and data management are hidden from the user.
#10. A ride-hailing service is another example of abstraction. The user interacts with the app to request a ride, while the underlying logistics and driver management are hidden from the user.
#11. A food delivery service is another example of abstraction. The user interacts with the app to order food, while the underlying logistics and restaurant management are hidden from the user.
#12. A music streaming service is another example of abstraction. The user interacts with the app to play music, while the underlying audio processing and data management are hidden from the user.
#13. A video conferencing app is another example of abstraction. The user interacts with the app to join meetings, while the underlying network protocols and video processing are hidden from the user.
#14. A fitness tracker is another example of abstraction. The user interacts with the app to track workouts, while the underlying sensors and data processing are hidden from the user.
#15. A smart thermostat is another example of abstraction. The user interacts with the app to set temperature preferences, while the underlying sensors and HVAC system management are hidden from the user.
#16. A smart lighting system is another example of abstraction. The user interacts with the app to control lights, while the underlying hardware and software work together to provide the desired functionality.
#17. A smart security system is another example of abstraction. The user interacts with the app to monitor security cameras and receive alerts, while the underlying hardware and software work together to provide the desired functionality.


#Code Example on A web browser of abstraction. solve the example using abstraction with less line of code as much as possible.
class Browser:
    def __init__(self, name):
        self.name = name

    def open(self, url):
        print(f"Opening {url} in {self.name} browser.")

    def close(self):
        print(f"Closing {self.name} browser.")
class Chrome(Browser):
    def __init__(self):
        super().__init__("Chrome")
    def open(self, url):
        print(f"Opening {url} in Chrome browser with Google services.")
    def close(self):
        print(f"Closing Chrome browser with Google services.")
class Firefox(Browser):
    def __init__(self):
        super().__init__("Firefox")
    def open(self, url):
        print(f"Opening {url} in Firefox browser with Mozilla services.")
    def close(self):
        print(f"Closing Firefox browser with Mozilla services.")
class Safari(Browser):
    def __init__(self):
        super().__init__("Safari")
    def open(self, url):
        print(f"Opening {url} in Safari browser with Apple services.")
    def close(self):
        print(f"Closing Safari browser with Apple services.")
class Edge(Browser):
    def __init__(self):
        super().__init__("Edge")
    def open(self, url):
        print(f"Opening {url} in Edge browser with Microsoft services.")
    def close(self):
        print(f"Closing Edge browser with Microsoft services.")
#Example usage:
chrome = Chrome()
chrome.open("https://www.google.com")
chrome.close()
firefox = Firefox()
firefox.open("https://www.mozilla.org")
firefox.close()
safari = Safari()
safari.open("https://www.apple.com")
safari.close()
edge = Edge()
edge.open("https://www.microsoft.com")
edge.close()
# #The above code demonstrates abstraction by defining a common interface for different web browsers without specifying how the methods are implemented. This allows us to create different browsers that implement the same interface, making it easier to work with different types of browsers in a consistent way.
# #Abstraction is a powerful concept that allows us to create flexible and reusable code. By defining a common interface for different classes, we can create systems that are easy to understand and maintain. This allows us to build complex systems while keeping the code organized and manageable.                
# #Abstraction is a key principle of object-oriented programming that helps to create robust and maintainable code. By abstracting away the implementation details, we can create objects that are easy to use and understand. This allows us to build complex systems while keeping the code organized and manageable.