#Welcome message
print("Welcome to the Fibonacci Generator!")
print("It will generate the nth number in the Fibonacci sequence for you.")
print("\n")

def fibonaci():
    #Get entry
    val = int(input("Enter n: "))

    #Fibonacci
    arr = [0,1]
    ans = 0
    k = 1
    for x in range(val+2):
        if(x >= 2):
            arr.append(arr[x-1] + arr[x-2])



    print("K("+str(val)+") = "+str(arr[val+1]))
    print(str(arr))

    y = input("Would you like to know another Fibonacci number?")
    if(y == "y" or y =="Y" or y == "Yes" or y == "yes"):
        fibonaci()

fibonaci()