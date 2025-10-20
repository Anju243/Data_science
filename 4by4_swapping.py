import numpy as np
x=np.arange(16,dtype='int').reshape(4,4)
print(x)
print("after swapping :")
x=x[[-1,1,2,0]]
print(x)