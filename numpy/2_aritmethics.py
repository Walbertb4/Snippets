import numpy as np

#----------------------- Scaler Aritmethic -----------------------

array= np.array([1,2,3])
print(array+1) # => [2 3 4]
print(array**3) # => [ 1 8 27]

#----------------------- Vectorized Aritmethic -----------------------
array= np.array([1.02,2.89,3.28])
print(np.sqrt(array)) # => [1.00995049 1.7        1.81107703]
print(np.round(array)) # => [1. 3. 3.] yuvarla
print(np.floor(array)) # => [1. 2. 3.] aşağı yuvarla
print(np.ceil(array)) # => [2. 3. 4.] yukarı yuvarla

radius=np.array([2,5,6])
print(np.pi * radius**2) # => Alan hesaplama

print(radius - array) # => [0.98 2.11 2.72]
print(radius * array) # => [ 2.04 14.45 19.68]
print(radius ** array) # => [  2.02791896 104.71847585 356.72709835]

#----------------------- Comparison Operators -----------------------

scores= np.array([55,100,98,2,38])
print(scores==100) # => [False  True False False False]
print(scores >=55) # => [ True  True  True False False]

scores[scores<60] = 0
print(scores) # => [  0 100  98   0   0]

