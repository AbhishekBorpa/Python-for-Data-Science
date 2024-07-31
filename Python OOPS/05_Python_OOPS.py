# access modifier -> making variable private and public according  to the user neccecity
# types 
"""
1. public -> import from outside 
2. private -> can't access from outside
3. protected -> access only from inside and subclass of that particalar class

"""
class employee:
  def __init__(self):
    self.name = "abhishek"
    self._age = 20 # protected
    self.__cls = 12



a = employee()
# class employee:
print(a.name) # public
print(a._age) # protected
# print(_employee__cls)


# super keyword






