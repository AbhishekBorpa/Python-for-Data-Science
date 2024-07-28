# user defined function ->  def name()
# rule are same as variable
a = 10
b = 20

# def add(p,q):
#   mean = (p*q)/(p+q)
#   # print(add)
#   return mean

# print(add(a,b))

# def WhoIsGreater(p,q):
#   if(p>q):
#     p = print("P is greater")
#     return p
#   else:
#     q = ("q is greater ")
#     return q

# print(WhoIsGreater(a,b))

# def sub():
#   pass # left for later 


# built-in -- google for more knowledge

# id(), iter()
 
# function arguments

# def average(c,d=150):
#   avg = print("the average is :",c+d/2)
#   return avg

# print(average(100))


# def average1(c,d=150): # value can in format b=10, a =12
#   avg = print("the average is :",c+d/2)
#   return avg

# print(average1(100))

# def average(c,d=150):
#   avg = print("the average is :",c+d/2)
#   return avg

# print(average(100))

def avg(*nummber): # take argument as tuple
  sum = 0
  for i in nummber:
    sum = i+sum
    average = print("avg is :",sum/(len(nummber)))
    return average
  


print(avg(10,20,30,40))

# def name(**naam):
#   print("hello",naam["fname"],naam["mname"],naam["lname"])


# print(name(fname="abhishek", mname="singh",lname= "kuntal"))






