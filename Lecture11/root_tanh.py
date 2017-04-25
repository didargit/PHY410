from root_finding import *
from math import *

def f ( x ) :
    return tanh(x)


print(" Algorithms for root of tanh(x)")
print(" ------------------------------------------------")

print(" 1. Secant Method")
xi = float ( input(" Enter initial guess xi : ") )
xf = float ( input(" Enter final guess xf : ") )
acc = float ( input(" Enter accuracy : ") )
answer = root_secant(f,xi,xf,acc,1000,True)
print  str ( answer ) + "\n\n"

print(" 2. Bisection search")

answer = root_bisection(f,xi,xf,acc,1000,True)
print  str ( answer ) + "\n\n"
