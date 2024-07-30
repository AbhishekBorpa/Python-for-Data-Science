# inheritence 
class employee:
  def __init__(self,name,id):
    self.id = id
    self.name = name

  def ShowDetails(self):
    print(f"id of Employes:{self.id} and name is {self.name}")

employee1 = employee("abhishek",10)
employee1.ShowDetails()


class programmer(employee):
  def ShowLanguage(self):
    print("Default language is python in computer ")


e2 = programmer("naveen singh",20)
e2.ShowDetails()
e2.ShowLanguage()


# types 
"""
1. single
2. multiple
3. multilevel
4. Hierircal
5. hybrid

"""


