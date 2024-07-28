import time

time_1= time.strftime('%H:%M:%S')
hour = int(input("enter your hour :"))
if(hour>=4 and hour<12):
   print("good morning")

elif (hour >=12 and hour <16):
   print("good afternoon")

elif(hour >=16 and hour< 19):

   print("good evening")

elif(hour>=19 and hour<24):
   print("good night")

print(time_1)