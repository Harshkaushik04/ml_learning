import numpy as np
import random
arr=np.arange(0,11)
print(arr[2])
print(arr[1:5])

#broadcasting
arr[1:5]=100
print(arr)
arr=np.arange(0,11)
print(arr)
sliced=arr[0:5]
print(sliced)
sliced[:]=100#by changing sliced array, original array also changes as its assigned to original
#if you want to not affect original, then make copy
print(arr)

#copy method-to not change array
arr=np.arange(0,10)
copy_sliced=arr[0:5].copy()
copy_sliced[:]=100
print(copy_sliced)
print(arr)

#indexing in 2d arrays
arr_2d=arr.reshape(2,5)
print(arr_2d.shape)
print(arr_2d)
print(arr_2d[1][3])#method 1 for indexing
print(arr_2d[1,3])#method 2 for indexing
print(arr_2d[:2,1:])#arr_2d[:2,1:]=arr_2d[:2][1:]
print(arr)
print(arr_2d>4)
#conditional selection
print(arr[arr>4]) #alternatively we can do bool_arr=arr>4 and write that instead of this

