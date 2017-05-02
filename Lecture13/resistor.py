from cpt import*
from numpy import*

vo = 4.5
r1 = 1
r2 = 1
r3 = 1
r4 = 1
r5 = 1
r6 = 1
r7 = 1
r8 = 1
r9 = 1
r10 = 1
r11 = 1
r12 = 1

r = Matrix(6,6)
r[0][0] = 1+1+1
r[0][1] = 1
r[0][2] = 1

r[1][0] = 1
r[1][1] = 1+1+1
r[1][4] = 1

r[2][0] = 1
r[2][2] = 1+1+1
r[2][3] = 1

r[3][2] = 1
r[3][3] = 1+1+1
r[3][5] = 1

r[4][1] = 1
r[4][4] = 1+1+1
r[4][5] = 1

r[5][3] = 1
r[5][4] = 1
r[5][5] = 1+1+1

Vt = Matrix(6,1)
Vt[0][0] = vo
Vt[1][0] = vo
Vt[2][0] = vo
Vt[3][0] = vo
Vt[4][0] = vo
Vt[5][0] = vo
print Vt
print r

r_save = Matrix_copy(r)
i = Matrix_copy(Vt)

solve_Gauss_Jordan(r, i)
print " Solution using Gauss-Jordan elimination"
print " i = "
print i
I =sum(i)
print I
Reffect = vo/I
print "The effective resistance is " + str(Reffect)


