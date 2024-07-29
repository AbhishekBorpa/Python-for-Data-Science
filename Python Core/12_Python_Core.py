# lambda function -> fn with no name and single line fn
# format : -> lambda var name: var_
double = lambda x: x**20
avg = lambda A,y: (A+y)/5
print(double(2))
print(avg(20,30))

def apply(fx,value):
  return 6+fx(value)

print(apply(lambda x: x**2,3))