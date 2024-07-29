# local and global variables
x = 5
print(x)

def num():
  global y
  x = 4
  y = 10
  return (f"local x is {x} ")
  return y


print(x)
print(num())
print(x)
print(y)