## intro to oops -> object orinted programming
class person:
  name= "abhishek"
  networth = 1200000
  age = 20
  def info(self):
    print(f"{self.name} is a {self.networth} money's owner and he is {self.age} year old")


a = person()
print(a.info())
a.age = 30
print(a.age)