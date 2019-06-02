import numbers

#Get 5 numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
d = int(input("Enter the fourth number: "))
e = int(input("Enter the firth number: "))

#Print the mean

mean = (a+b+c+d+e)/5
print("Mean is: "+str(mean))

#Id the number a muliple of 3 or 5 or both

def checkMultiple(num):

    if((num % 5) == 0 and (num % 3) == 0):
        print(str(num)+" is a multiple of both 3 and 5")
    elif((num % 5) == 0):
        print(str(num)+" is a multiple of 5")
    elif ((num % 3) == 0):
        print(str(num) + " is a multiple of 3")

checkMultiple(a)
checkMultiple(b)
checkMultiple(c)
checkMultiple(d)
checkMultiple(e)