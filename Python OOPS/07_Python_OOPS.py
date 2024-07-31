# class variables and class variable
# class emp:
#   company_name = "apple" # class variables
#   def __init__(self,name,age):
#     self.name = "jeetu"
#     self.age = 20

#   def showDetails(self):
#     print(f"my name is {self.name} and i am {self.age} and work at {self.company_name}")

# # here aa is an instance
# aa = emp("Abhishek",20)
# aa.age = 20
# aa.name ="deepak" # instance variable


# print(aa.showDetails())
# # emp.showDetails(aa) # same as above two lines

# bb = emp("none",11)

# class methods as alterantive Constructors
class emp2:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  @classmethod # -> used for specific purpose
  def fromstr(cls,string):
    return cls(string.split("-")[0],string.split("-")[1])
e = emp2("Abhishek Singh",20)
print(e.age)
print(e.name)

string = "Room-134"
e = emp2.fromstr(string)
print(e.name)
print(e.age)