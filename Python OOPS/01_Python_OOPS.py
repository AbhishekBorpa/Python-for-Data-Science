# ## intro to oops -> object orinted programming
# class person:
#   name= "abhishek"
#   networth = 1200000
#   age = 20
#   def info(self):
#     print(f"{self.name} is a {self.networth} money's owner and he is {self.age} year old")

# a = person()
# print(a.info())
# print(a.networth)
# # a.age = 30
# # print(a.age)
# b = person()
# b.name = "Naveen Singh"
# b.networth = 12000
# b.age = 16
# b.info()


# constructor for initialisation -> create and initilize objects

# class person:
#   def __init__(self,N,oc):
#     self.name = N
#     self.occ = oc
    
  
#   def abhi(self):
#     # print("next line")
#     # print(" hey over there")
#     print(f"{self.name} is  a {self.occ}")
#   # name= "abhishek"
  # networth = 1200000
  # age = 20
  # def info(self):
  #   print(f"{self.name} is a {self.networth} money's owner and he is {self.age} year old")


# a = person("abhishek","hr")
# a.abhi()
# b = person("naveen","engineer")
# b.abhi()
# b = person()

# parametratized constructor -> where we give parameter
# default -> when it has only self parameter


# decorator -> modify the behavior of function and methods


# *args  = take input as tuple 
# **kwargs = take input as dictionary

def greet(fx):
  def mfx(self,*args,**kwargs):
    print("good morning")
    fx(*args,**kwargs)
    print("Thanks for using this function")
    return mfx

class Person():
  def __init__(self,name,age):
    self.name = name
    self.age = age
    print(f"person {self.name} is {self.age} is year old")


  @greet
  def hello(self):
    print(f"{self.name} is saying { self.age}")

  def __del__(self):
        # Destructor
    print(f"Person {self.name} is being deleted")


# say hello
person1 = Person("abhishek",29)
# print(Person.hello())
print(person1)