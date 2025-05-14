#Encapsulation Concept.
#Encapsulation is a concept of Object-Oriented Programming (OOP) that binds together the data and the functions that manipulate that data, restricting access to some of the object's components. This is a protective barrier that keeps the data safe within the object and prevents outside code from directly accessing it. Encapsulation helps in hiding the internal state of an object and requires all interaction to be performed through an object's methods.
#In Python, encapsulation is implemented using private and public access specifiers. By default, all class members (attributes and methods) are public. To make a member private, we can prefix its name with a double underscore (__). This makes it inaccessible from outside the class.
#We can also use a single underscore (_) to indicate that a member is intended for internal use only, but this is just a convention and does not enforce access restrictions.
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New balance: {self.__balance}")
        else:
            print("Withdrawal amount exceeds balance or is not positive.")

    def get_balance(self):
        return self.__balance  # Public method to access private attribute __balance
    #Example usage:
account = BankAccount("123456789", 1000)
account.deposit(500)  # Deposited: 500. New balance: 1500
account.withdraw(200)  # Withdrew: 200. New balance: 1300
print(account.get_balance())  # 1300
# The above code demonstrates encapsulation by restricting direct access to the account number and balance attributes. 
# Instead, we provide public methods to interact with the account, ensuring that the internal state is managed properly.
#Encapsulation is a fundamental concept in object-oriented programming that helps to protect the internal state of an object and provides a clear interface for interacting with that object. By using private and public access specifiers, we can control access to the data and methods of a class, ensuring that the internal state is only modified in controlled ways. This helps to maintain the integrity of the object's data and makes it easier to understand and maintain the code.
#Encapsulation is a key principle of object-oriented programming that helps to create robust and maintainable code. By encapsulating data and behavior within classes, we can create objects that are self-contained and easy to work with. This allows us to build complex systems while keeping the code organized and manageable.
#Encapsulation is a powerful concept that allows us to create objects that are easy to use and understand. By encapsulating data and behavior within classes, we can create objects that are self-contained and easy to work with. This allows us to build complex systems while keeping the code organized and manageable.