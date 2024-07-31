# access modifier -> making variable private and public according  to the user neccecity
# types 
"""
1. public -> import from outside 
2. private -> can't access from outside
3. protected -> access only from inside and subclass of that particalar class

"""
# class employee:
#   def __init__(self):
#     self.name = "abhishek"
#     self._age = 20 # protected
#     self.__cls = 12



# a = employee()
# # class employee:
# print(a.name) # public
# print(a._age) # protected
# # print(_employee__cls)


# super keyword
# class parmeth:
#   def __init__(self):
#     print("hello")
#   def parmet(self):
#     print("this is parent method")

# class childmeth(parmeth):
#   def parmet(self):
#     print("abhishek")
#     super().__init__() # super () methods
#   def child_method(self):
#     print("new child methods")
#     super().parmet()

# child_obj = childmeth()
# child_obj.child_method()
# child_obj.parmet()


# magic and dunder methods

# __init__ methods


# class emp3:
#   name = "abhishek"
#   def __init__(self,name):
#     self.name = name
#   def __len__(self):
#     i = 0
#     for c in self.name:
#       i = i +1
#     return i


# e = emp3("abhishek")
# print(e.name)
# print(len(e))

# ========= method overiding  ================

# make changes in original code for new task using super function




