import numpy as np

"""
Single dimensional 
"""

arr=np.array([4,6,7,8])

print(type(arr)) #<class 'numpy.ndarray'>
print(arr.shape) #(4,)

print(arr[2]) #7

"""
Multi Dimensional array
"""

two_d=np.array(([1,4,9],[1,2,7]))
print(two_d.shape) #(2, 3)

"""
Zero array
"""

zeros=np.zeros((2,3))
print(zeros) 

"""
ones array
"""

ones=np.ones((4,2))
print(ones)

"""
Array of evenly spaced values
"""

val=np.arange(10,25,5)
print(val)

"""
nxn identity matrix
"""
im=np.eye(2)
print(im)

"""
array operations elementwise (vectorised matrix operation)
"""
a=np.array(([1,2,3],[2,6,3]))
b=np.array(([2,1,3],[0,1,1]))

print(a+b)
print(np.add(a,b))


"""
array transpose
"""
m1=np.array(([1,2],[3,4],[5,6]))
print(m1)
print(np.transpose(m1))    
print(m1.T)    

"""
Broadcasting
"""
m2=np.array(([1,2,3],[2,6,3]))
print(m2+5)