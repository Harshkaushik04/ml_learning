import numpy as np
arr=np.arange(0,10)
print(arr)
arr+=5
print(arr)
arr+=arr
print(arr)
arr-=arr
print(arr)
arr=np.arange(0,100,5)
print(arr)
print(np.sqrt(arr))
print(np.log(arr[1:]))
print(arr.sum())
print(arr.mean())
print(arr.var())
print(arr.std())
arr_2d=np.arange(0,25).reshape(5,5)
print(arr_2d)
print(arr_2d.sum())
print(arr_2d.sum(axis=0)) #sum of columns
print(arr_2d.sum(axis=1)) #sum of rows
