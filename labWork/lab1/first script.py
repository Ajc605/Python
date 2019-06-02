# get inputs
a = input("Input a: ")
b = input("Input b: ")
c = input("Input c: ")
m = input("Input m: ")
n = input("Input n: ")
o = input("Input o: ")

equation = a+"x^"+m+"+"+b+"X^"+n+"+"+c+"x^"+o
print(equation)

a = int(a) * int(m)
b = int(b) * int(n)
c = int(c) * int(o)
m = int(m) -15
n = int(n) - 1
o = int(o) - 1

equation = str(a)+"x^"+str(m)+"+"+str(b)+"X^"+str(n)+"+"+str(c)+"x^"+str(o)
print(equation)
