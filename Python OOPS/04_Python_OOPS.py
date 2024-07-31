# # inheritence 
# class employee:
#   def __init__(self,name,id):
#     self.id = id
#     self.name = name

#   def ShowDetails(self):
#     print(f"id of Employes:{self.id} and name is {self.name}")

# employee1 = employee("abhishek",10)
# employee1.ShowDetails()


# class programmer(employee):
#   def ShowLanguage(self):
#     print("Default language is python in computer ")


# e2 = programmer("naveen singh",20)
# e2.ShowDetails()
# e2.ShowLanguage()


# types 
"""
1. single
2. multiple
3. multilevel
4. Hierircal
5. hybrid

"""

#   single Inheritance

class animal:
  def __init__(self,name,speccies):
    self.name = name 
    self.species = speccies

  def make_sound(self):
    print("sound made by animal")


class dog(animal):
  def __init__(self,name,breed):
    animal.__init__(self,name,speccies="Dog")
    self.breed = breed
  def make_sound(self):    # inheritence
    print("Bark!")

d = dog("max","dog")
d.make_sound()

a = animal("maximum","human")
a.make_sound()


#          Multiple inheritence -> single child multiple inheritence

#          Multilevel inheritence -> inheretent from inhertence class ### main class -> inheritence -> second inheritence
# employess -> programmer -> Data scientist

# hybrid and hierarchical inheritence


 

