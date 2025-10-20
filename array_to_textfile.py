import numpy as np
x=np.arange(16).reshape(4,4)
print("array:")
print(x)

header='c1,c2,c3,c4'
np.savetxt('array.txt,x,fmt="%d",header=header')
print("after loading content of text file")
print(np.loadtxt('array.txt'))