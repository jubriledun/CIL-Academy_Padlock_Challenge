#Padlock Code Challenge - www.101computing.net/padlock-code-challenge-2/
import random
code = 0
initial_list=[]
final_list=[]
#Update the code below to solve this challenge
for digit1 in range(0,10):
  for digit2 in range(0,10):
    for digit3 in range(0,10):
        initial_list.append(str(digit1)+str(digit2)+str(digit3))
        

for i in initial_list:
     for j in i:
        if i[0]<i[1]<i[2]:
           final_list.append((i[0]+i[1]+i[2]))


code = random.choice(final_list)
print("Code:")
print(code)