import random
maxrandom = 80
minrandom = 1
r = random.randint(minrandom,maxrandom)
while True :
    n = int(input("what number am i thinking through " + str(minrandom)+"-"+str(maxrandom)+":"))
    if r == n :
        print(" you guessed the number!",r)
        break
    if n > r:
        print("the number is lower")
        continue
    if n < r:
        print( " the number is higher")
        continue
