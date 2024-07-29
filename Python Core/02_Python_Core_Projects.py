# display questions to user -> KBC Game

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language is best for AI Programming?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]

questions = ["which language was used to create fb?","Python","French","PHP","None",4]


levels = [1000,2000,5000,10000,20000,40000,80000,160000,320000]

for i in range(0,len(questions)):
  question = questions[i]
  print(f"Question for Rs.{levels[i]}")
  print(f"a.{question[1]}       b.{question[2]}")
  print(f"c.{question[3]}       d.{question[4]}")

  reply = int(input("enter your answer(1-4)"))
  if (reply==0):
    money = levels[i-1]
    break
  if reply==questions[-1]:
    print(f"Correct answer, You have own Rs. {levels[i]}")
  if (i ==4):
    money = 10000

  elif(i==9):
    money= 320000
  elif(i==14):
    money= 500000
  else:
      print("no money ")
else:
  print("Wrong Answer")





















