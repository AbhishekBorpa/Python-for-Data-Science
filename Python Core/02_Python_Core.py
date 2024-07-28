# tuple : immutable data-type

# tpl = ('abhishek',12,True)
# print(tpl)
# # tpl[0] = 10
# print(len(tpl))
# print(tpl[0])

# tpl_1 = (1,)
# print(tpl_1,type(tpl_1))
# if 12 in tpl:
#   print("yes")
# else:
#   print("nooooo")

# # slicing
# print(tpl[:-1])

# methods

# to make changes in tuple in you must have to convert them in list first after change convert them in tuple back
countries = ("india","china","nepal","france","italy","rome","america","india")
print(countries)
tpl = list(countries)
print(tpl)
# now we can apply any list methods
countries = tuple(tpl)
print(countries)
print(countries.count("india"))
print(countries.index("china"))
print(countries.index("india",4,9)) # in given range