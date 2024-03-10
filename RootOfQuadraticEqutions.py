a = int(input('enter numeric value of x squar '))
b = int(input('enter numeric value of x '))
c = int(input('enter numeric value of C '))
import math

r1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
r2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)


print('roots of given Quadratic Equations is ',r1,' & ', r2)

