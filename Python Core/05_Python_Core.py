# exceptional handling
# try... except code
# python have lots of prebuilt function
# try:
#   a = int(input("enter a num : "))

#   print(f" multiplcation table of {a} is :")

#   for i in range(11):
#     print(f"{int(a)}X{i}={int(a*i)}")
# # except Exception as e
#   # print(e)
# except IndexError:
#   print()


print("okk program have run")


# use finally 

# try:
#   a = int(input("enter a num : "))

#   print(f" multiplcation table of {a} is :")

#   for i in range(11):
#     print(f"{int(a)}X{i}={int(a*i)}")
# # except Exception as e:
#   # print(e)
# except IndexError:
#   print()
# finally:      # always  execute and valuable of when used in function
#   print("no Way")




# custome error
a = int(input("enter integer between 5 and 10: "))
if(a<5) or (a>10):

  raise ValueError()
print("done :",a) # know more on youtube