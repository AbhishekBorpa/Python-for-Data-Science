def log_method_call(method):
    def wrapper(self, *args, **kwargs):
        print(f"Calling {method.__name__} with arguments: {args} {kwargs}")
        result = method(self, *args, **kwargs)
        print(f"{method.__name__} returned: {result}")
        return result
    return wrapper

class Person:
    def __init__(self, name, age):
        # Constructor
        self.name = name
        self.age = age
        print(f"Person {self.name} created, age {self.age}")

    @log_method_call
    def introduce(self):
        # Method to introduce the person
        return f"Hi, I'm {self.name} and I am {self.age} years old."

    def __del__(self):
        # Destructor
        print(f"Person {self.name} is being deleted")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Using the method to introduce the person
print(person1.introduce())

# Deleting the instance explicitly (optional, for demonstration)
del person1
