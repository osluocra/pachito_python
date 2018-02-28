# Guess the number
import random
maxrandom = 100
minrandom = 1
r = random.randint(minrandom,maxrandom)

#print( "number that you entered is:",n)
# print(" the random number is :",r)

while True :
    n = int(input ("what number am i thinking through " + str(minrandom)+"-"+str(maxrandom)+ ":"))
    if r == n :
        print("you guessed the number",r)
        break
    if n > r :
        print(" the number is lower")
        continue
    if n < r :
        print( " the number is higher")
        continue 

    

