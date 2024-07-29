# # file handling
# fil = open('Python Core/file.txt','r') # r for read mode and it is default.
# print(fil)
# text = fil.read()
# print(text)
# fil.close()

"""
File modes : r-> read and default
w -> write and create if not available previoulsy
A -> append create content in last of file
t -> text and default
b -> binary 
"""

# write mode

wrt = open('file_1.txt','w')
wrt.write('my name is abhishek')
# wrt.close()


# with statement

with open('Python Core/file_1.txt','a') as f:
  wrt.write(" i am here new")

  # wrt.close()

