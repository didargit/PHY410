from trapezoid import *
from simpson import *
from math import *

num1 = 10000
num2 = 0
d = exp

while num1 % 2 != 0 :
    num1 = int(raw( "Enter even number of intervals for trapezoidal rule" ))

a = 0
b = log(e)

answer1 = trapezoid(d,a,b,num1)
print 'Trapezoidal rule = ' + str(answer1)

answer2 = simpson(d,a,b,num1)
print 'Simpson rule = ' + str(answer2)



