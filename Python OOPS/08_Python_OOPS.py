# object introspection -> find ways and methods for better use

# dir()
x = [1,2,3,4]
# print(dir(x))


# __dict__ options
# class per:
#   def __init__(self,name,age,ver):

#     self.name = name
#     self.age = age 
#     self.ver= 2

# p = per("Abhi",22,12)
# print(p.__dict__)
# print(help(list))

from new import emp3

e = emp3("naveen")
print(e.name)
