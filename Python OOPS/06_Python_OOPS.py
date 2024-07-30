# static Method 

class Maths:
  def __init__(self,num):
    self.num = num

  def autonum(self,n):
    self.num = self.num+n

  @staticmethod
  def add(a,b):
    return a+b
  


d = Maths(5)
print(d.num)
d.autonum(20)
print(d.num)
# print(d.add(20,30))
print(Maths.add(30,40))
