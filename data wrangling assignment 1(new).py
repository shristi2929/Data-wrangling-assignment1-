#1. Create a null vector of size 10 but the fifth value which is 1.

import numpy as np

n = np.zeros(10)
n[4]=1
n

##2. Create a vector with values ranging from 10 to 49.

m =  np.arange(10,50)
m

##3. Create a 3x3 matrix with values ranging from 0 to 8

z = np.arange(0,9)
m = z.reshape(3,3)
m

##4. Find indices of non-zero elements from [1,2,0,0,4,0]

l = np.array([1,2,0,0,4,0])
z = np.where(l>0)
print("Indices of non-zero elements are ",z)
l = np.array([1,2,0,0,4,0])
print("Indices of non-zero elements are : ")
for i in range(len(l)):
    if l[i] !=0:
        print(i,end = " ")

##5. Create a 10x10 array with random values and find the minimum and maximum values.

o = np.random.randint(0,50,(10,10))
print(o)
p = np.max(o)  #o.max()
print("The maximum value is :",p)
q = np.min(o)   #o.min()
print("The maximum value is :",q)

## 6. Create a random vector of size 30 and find the mean value.

t = np.random.rand(30)
y = t.mean()
y
y = np.random.randint(2,90,30)
z=y.mean()
z