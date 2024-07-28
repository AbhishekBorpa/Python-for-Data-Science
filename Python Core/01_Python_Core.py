# List use for storing multiple value in single variable name

abhishek = ["abhishek singh","deep singh","Naveen Singh","Naveen Singh",10,20,30,True,20.5]
# print(abhishek[6:]) # indexing
# print(abhishek[1:20:2]) step of 2
# print(abhishek[1:-1]) start at 1 and end at -1 but not include it
# print(abhishek[-6:-1]) # negative indexing
# if 10 in abhishek: # can be used in string check in or not in operators
#   print("Yes")

# else:
#   print("noooooo")
# print(abhishek)

# # list comprehention 
# lst = [ i+1 for i in range(10) if i%2!=0]
# print("lst : ",lst)
# nam = [p for p in abhishek ]
# print(nam)

# list methods 

num = [1,2,3,4,5,6,7,8,9,9,9,10]
print(num)
num.append(11) # add value in end
num.sort(reverse=True) # reverce the  order
num.reverse() # reverce the  List
print(num.index(5))


print(num)
print(num.count(9))
nums = num # make change in both 
nums.append(111)
print(nums)
print(num)

num_2=num.copy() # no change in original
num_2.append(123)
print(num)


num_2.insert(2,11)
print(num_2)

num_2.extend(abhishek)
print(num_2)
# print(abhishek.reverse())
# # print(abhishek.index())
# print(abhishek.pop())
# print(abhishek)
