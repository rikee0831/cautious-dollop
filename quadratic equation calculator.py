a = input("coefficient of x^2?")
a = float(a)
b = input("coefficient of x?")
b = float(b)
c = input("coefficient of x^0?")
c = float(c)
x1 = (-b+(((b**2)-4*a*c)**0.5))/(2*a)
x2 = (-b-(((b**2)-4*a*c)**0.5))/(2*a)
print(x1,x2)
x3 = x1+6.66
x4 = x2+6.66
SOR = x3+x4
POR = x3*x4
print ("x^2",-SOR,"x+",POR,"=0")