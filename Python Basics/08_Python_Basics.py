# String
name = "abhishek singh"
name_2 = "deepak Singh"
# name_3 = name+name_2
# print(name_3)

name_4 = """ hey Abhishek Singh this is python program for learning more about string functions New""" 
# it can be single string ''' like this '''
#print(name_4[2:10])

# for i in name_4:
#     print(i)
#     print("New Line \n")

# String Slicing

# print(name_4)
# print(len(name_4))
# print(name_4[:14])
# print(name_4[2:25:2])
name_5 = "ABhishek Singh"
# print(name_5[-10:-1])
# print(name_5[0:4])
print(name_5[-5:9])

# string Methods
print(name_5.upper())
print(name_5.lower())
print(name_5.rstrip("k"))
print(name_5.replace("Singh","kuntal"))
print(name_5.split("i"))

print(name_2.capitalize())
print(name_4.count("in"))

print(name_4.endswith("New"))
print(name_4.find("is")) # index()  for error message
# isalpha(), isalnum(), islower(), isprintable(), istitle(), swapcase(lower -> upper case, vice-versa), title()
