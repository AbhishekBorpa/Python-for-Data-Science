# match case -> if value match
import os 
os.system("python --version")
val = int(input("enter a value :"))
match val:
  case 1:
    print("x is 1")
  case 2:
    print("case is 2")
  case 3 :
    print("case is 3")
  case _ if val !=20 :
    print("i like it")