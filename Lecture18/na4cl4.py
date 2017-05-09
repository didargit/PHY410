from nacl import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
 
name="Na4Cl4"      
nNa = 4
nCl = 4
n = nNa + nCl
a = 0.6


#r_Na = [  [ .2*a, .7*a, .7*a], [ .2*a, .7*a, -.7*a], [ -.4*a, a, 0], [ .1*a, 2*a, 0] ]
#r_Cl = [  [ 0, 0, 0], [ -.4*a, .7*a, 0], [ .2*a, a, 0], [ -.2*a, 2*a, 0] ]

r_Na = [  [ 0, 0, 0], [ .7*a, 0.1*a, .5*a], [ 0.2*a, a, -.5*a], [ 0, 1.2*a, -a] ]
r_Cl = [  [ .4*a, -.1*a, .45*a], [ .6*a, a, -.45*a], [ 0, 1.3*a, -.1*a], [ 0, .2*a, -a] ]

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
