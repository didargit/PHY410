from nacl import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
name="Na3Cl3"      
nNa = 3
nCl = 3
n = nNa + nCl
a = 0.3

r_Na = [  [ 0.5*a, 0, 0 ], [ 2*a, .866*a, 0], [0.5*a,1.732*a,0] ]
r_Cl = [  [ 0, 0.866*a, 0 ], [ 1.5*a, 0 , 0 ], [1.5*a,1.732*a,0] ]

cluster = Cluster()
 
for i in xrange(nNa) :
     r = Vector(r_Na[i])
     cluster.add(Na(r))
 
for i in xrange(nCl) :
     r = Vector(r_Cl[i])
     cluster.add(Cl(r))
 
print " " + name + " cluster"
print " Initial potential energy = " + str( cluster.potential_energy() )
 
# Minimize the function
accuracy = 1e-6
 
res = cluster.minimize( accuracy )
 
pe = res[1]
iterations = res[4]

print " Minimized potential energy = " + str(pe) + " eV"
print " Binding energy of cluster  = " + str( pe / 2.0 ) + " eV"
print " Number of function calls = " + str( iterations )

file_name = name + ".data"
outfile = open( file_name, 'w' )
for i in xrange( nNa + nCl - 1) :
    for j in range(i+1,nNa+nCl) :
        rij = cluster.ion(i).r - cluster.ion(j).r
        dr = sqrt( np.dot(rij,rij) )
        s =  "(" + cluster.ion(i).name + ")-(" + cluster.ion(j).name + ")"
        print " " + s + " r_" + str(i) + str(j) + " = " + str( dr ) + " nm"

outfile.write( str(cluster) )
outfile.close()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

[x,y,z] = cluster.convert()
ax.scatter( x,y,z )
plt.show()
