import numpy as np
import random
my_list=[1,2,3]
print(type(my_list))
my_array=np.array(my_list)
print(my_array)
print(type(my_array))
my_matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(my_matrix)
matrix=np.array(my_matrix)#numpy creates nested list into matrix
print(matrix)
print(np.arange(0,10,2))#creates list of numbers between 0 to 10(not including 10), with interval of 2
print(np.zeros(5))#1d array of 5 zeros
print(np.zeros((2,5)))#2d array
print(np.ones((4,4)))#2d array
print(np.linspace(0,10,3))#both 0 and 10 are included and 3 numbers to be chosen between
print(np.linspace(0,10,11))
print(np.eye(5))#identity matrix
print(np.random.rand(4,6))#uniform distribution #matrix of 4 vs 6 random number between 0 and 1(1 exclusive)
print(np.random.randn(4,6)) #standard normal distribution-mean=0,variance=1
print(np.random.randint(1,101,(4,6))) #1 is inclusive and 101 is exclusive-uniform distribution of integers
np.random.seed(42) #to generate a particular set of random numbers
print(np.random.rand(4))
print(np.random.rand(5))
arranged=np.arange(0,25)
print(arranged)
rearranged=arranged.reshape(5,5) #reshaping arranged into 5*5 matrix
print(rearranged)
random_array=np.random.randint(0,101,10)
print(random_array)
print(random_array.max()) #for finding max
print(random_array.min())#for finding min
print(random_array.argmax())#for finding index of max
print(random_array.argmin())#for finding index of min
print(random_array.dtype)
print(random_array.shape)#finding shape, (10,) represents 1d array
reshaped_random_array=random_array.reshape(2,5)
print(reshaped_random_array)


