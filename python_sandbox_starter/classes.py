# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class

class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    def has_birthday(self):
        self.age += 1


# Extend class
class Customer(User):
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    #Overwrote greeting method in parent
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and my balance is {self.balance}'

# Initialize user object

brad = User('Brad Traversy', 'brad@gmail.com', 37)


# Init a customer
janet = Customer('Janet Jonson', 'janet@gme.com', 28)

janet.set_balance(500)
#Can still call all methods in parent class because it extends it
print(janet.greeting())

brad.has_birthday()

print(brad.greeting())
