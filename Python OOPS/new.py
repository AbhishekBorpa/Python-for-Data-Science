class emp3:
  name = "abhishek"
  def __init__(self,name):
    self.name = name
  def __len__(self):
    i = 0
    for c in self.name:
      i = i +1
    return i


e = emp3("abhishek")
print(e.name)
print(len(e))