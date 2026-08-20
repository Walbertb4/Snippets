import numpy as np

#Numpy ile array oluşturma
array= np.array([1,2,3,4])

#Python listesi ile numpy listesi farkı
my_list=[1,2,3,4]
my_list=my_list*2
#print(my_list) => [1,2,3,4,1,2,3,4]
array=array*2
#print(array) => [2 4 6 8]

#Numpy ile virgüllü gösterim, string olarak
print(repr(array))


#-----------------------Dimensions -----------------------
#Eleman sayıları eşit olmalı
array.ndim # => kaç dimension olduğunu gösterir
print(np.array("a").ndim) # => 0 dimension
print(np.array([1,2,3,4,5]).ndim) # => 1 dimension
print(np.array([["a","b","c"],["a","b","c"],[1,2,3]]).ndim) # => 2 dimension, 3x3 matrix

# 3 Dimension Array
array_3d = np.array([
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]],

    [[13, 14, 15, 16],
     [17, 18, 19, 20],
     [21, 22, 23, 24]]
])

#Matrix boyutunu gösterme
print(np.array([1,2,3,4,5]).shape) # => (5,) 
print(np.array([["a","b","c"],["a","b","c"],[1,2,3]]).shape) # => (3,3)
array_3d.shape # => (2, 3, 4) katman sayısı, satır sayısı, sütun sayısı

#Chain Indexing (python)
print(array_3d[0][0][0]) # => 1

#Multidimensional Indexing (numpy)
print(array_3d[0,0,0]) # => 1


#-----------------------Slicing-----------------------
array1_2d=np.array([[1,2,3,4],
                    [5,6,7,8],
                    [9,10,11,12],
                    [13,14,15,16]]) #4x4 matrix