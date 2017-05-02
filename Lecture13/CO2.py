from cpt import *
 
Om = 16.0 #atomic mass of oxygen
Cm = 12.0 #atomic mass of carbon

# Calculating the (5,5) matrix with masses in the diagonal 
Calculate = Matrix(5,5)
Calculate [0][0] = Om
Calculate [1][1] = Cm
Calculate [2][2] = Cm
Calculate [3][3] = Cm
Calculate [4][4] = Om
print "Calculate  = "
Matrix_print(Calculate)

[detCalculate , Calculateinv] = inverse(Calculate )
print "Calculate inv = "
Matrix_print(Calculateinv)



kco = 140000
kcc = 150000

K = [
    [   kco,     -kco,        0.0,     0.0,    0.0     ],
    [   -kco,    kco+kcc,     -kcc,      0.0,    0.0     ],
    [   0.0,    -kcc,       kcc+kcc,    -kcc,    0.0     ],
    [   0.0,    0.0,        -kcc,     kco+kcc,  -kco     ],
    [   0.0,    0.0,        0.0,     -kco,     kco     ],
]

print "K = "
Matrix_print(K)

# Solve with generalized eigenvector solution
[ eigenvalues, eigenvectors ] = solve_eigen_generalized(K, Calculate)

print "Eigenvalues ="
print eigenvalues
print "Eigenvectors ="
Matrix_print(eigenvectors)
