from random import *

#Start
#Choose and number and say so
num = randint(1, 100)
cnt = 1
print("Game is ready")

while(True):
    x = int(input("Make a guess: "))
    if(x == num):
        print("well done that is correct")
        break
    elif(x > num):
        print("That's too high")
    else:
        print("That's too low")

    cnt += 1
print("that took "+str(cnt)+" guesses")
print("Bye")