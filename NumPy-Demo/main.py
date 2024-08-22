import numpy as np

# Creating numpy array
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# Creating arrays of different dimensions
arr1 = np.array(42) # Scalar
arr2 = np.array([1, 2, 3, 4, 5]) # 1-D
arr3 = np.array([[1, 2, 3], [4, 5, 6]]) # 2-D

# Check the dimension
print(arr1.ndim, arr2.ndim, arr3.ndim)

# Indexing is the samae
print(arr2[0], arr2[1:])

print(arr3.shape) # (Dimension, number of elements inside each array)

# Shaping arrays (only works if possible)
arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
new_arr = arr4.reshape(4, 3)
print(new_arr)
