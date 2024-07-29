# lambda function -> fn with no name and single line fn
# format : -> lambda var name: var_
# double = lambda x: x**20
# avg = lambda A,y: (A+y)/5
# print(double(2))
# print(avg(20,30))

# def apply(fx,value):
#   return 6+fx(value)

# print(apply(lambda x: x**2,3))


# # map(), reduce() and filter()

# # map() -> apply a fn to collection of value and a higher order function(fn who can get other function as input)
# def cube(x):
#   return x*x*x

# l = [11,21,23,24,25,16]
# # newl = list(map(cube,l))
# newl = list(map((lambda x:x*x*x),l))
# print(newl)

# # filter()
# def filter_function(a):
#   return a>18
# newline = list(filter(filter_function,l))
# print(newline)

# reduce() # it have to be import

from functools import reduce
# sum take two val and remove num and sum value 

num = [1,2,3,4,5,6,7]
def mysum(x,y):
  return x+y
sum = reduce(mysum,num)
print(sum)