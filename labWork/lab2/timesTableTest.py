from random import  *

#Start
cnt = 0
for x in range(10):
    #choose two random numbers
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    #Display the numers

    userAnswer = int(input(str(num1)+" x "+str(num2)+"="))

    #Calculate correct answer
    answer = num1*num2

    #Check answer
    if(answer == userAnswer):
        print("That’s correct, well done.")
        cnt = cnt +1
    else:
        print("Sorry, the right answer is "+str(answer))

#Dislay summary
print("You got "+str(cnt)+" out of 10 correct")

#End