import numpy as np
x=np.arange(21)
print("vector:")
print(x)

print("after change the sign of numbers in the range 9 to 15:")
x[(x>=9)&(x<=15)]*=-1
print(x)