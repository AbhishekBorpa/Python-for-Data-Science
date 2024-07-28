# sets : group of numbers : unordered collection of data 

sets = {2,3,4,5,7,8}
sets_4 = { 4,5,6,7,8,9,10}
# sets_2 = {2,3,4,"abhishek",True,34.52}
# print(sets)
# print(type(sets))
# sets_3 = set()
# print(type(sets_3))

print(sets,sets_4)
# print(sets.union(sets_4))
# sets.update(sets_4)
print(sets)

print(sets.intersection(sets_4))
print(sets.symmetric_difference(sets_4))
print(sets_4.difference(sets))
print(sets.isdisjoint(sets_4))
print(sets.issuperset(sets_4))
sets.add(12)
pops=sets.pop()
sets.remove(4)
sets.remove(3)
print(sets)
print(pops)
if 4 in sets:
  print("yes")
else:
  print("nooooo")
del pops