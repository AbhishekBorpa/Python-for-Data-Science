# break and continue
# break
for m in range(15):
  if(m == 10):
      break  # leave the loops
  print(" 5 X",m+1,"=",5*(m+1))


print("mamla done")

# continue
for i in range(15):
  if(i == 10):
     if i==10:
      print("eleven is missing")
     continue # left value when i==11 only
     
  print(" 5 X",i+1,"=",5*(i+1))

# while 
n = 0
while n<11:
  print(n+1)
  n = n+1
  if n ==10:
    break
    print("new life")


# do while

# p =1

# do {
#    print(p+1);
# } while (p<10);