import numpy as np
import math
p = np.array(eval(input('Enter 3 points of a circle, ex. [1,2],[3,4],[5,6]: ')))
k1 = -(p[0,0]**2 + p[0,1]**2)
k2 = -(p[1,0]**2 + p[1,1]**2)
k3 = -(p[2,0]**2 + p[2,1]**2)
a3 = np.array([1,1,1])
A = np.c_[p,a3]
B = np.array([k1,k2,k3])
[D,E,F] = np.linalg.solve(A,B)
h = -D/2
k = -E/2
r = math.sqrt((D**2+E**2)/4-F)
c = np.array([h,k])
Def = np.array([D,E,F])
print('center is on ',c)
print('radius is ',r)
print('vector [D,E,F] is',Def)