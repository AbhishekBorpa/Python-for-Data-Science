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

# wrt = open('file_1.txt','w')
# wrt.write('my name is abhishek')
# # wrt.close()


# # with statement

# with open('Python Core/file_1.txt','a') as f:
#   wrt.write(" i am here new")

  # wrt.close()


# f = open('file_new.txt','w')
# # while True:
# #   line = f.readline()
  
# #   if not line:
# #     break 
# #   print(line)


# lines = ['line 1 \n','line 2 \n','line 3 \n']
# f.writelines(lines)
# f.close()

# seek() tell()
# seek() start reading file after a certain period

with open('file_1.txt','r') as f:
  print(type(f))
  # f.truncate(5) # make sure only 5 character in file 
  f.seek(10)
  print(f.tell()) # tell return location of seek
  data = f.read()
  print(data)



