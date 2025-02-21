import numpy as np

print("Currently Running: NumPy",np.__version__)


array = np.array([1,2,3,4,5])
print("NumPy Array: ",array)
print("Array Type: ",type(array))

print("- - -")

zerodarray = np.array(42)
print("NumPy",zerodarray.ndim,"D Array: ")
print(zerodarray)

print("- - -")

onedarray = np.array([1,2,3,4,5])
print("NumPy",onedarray.ndim,"D Array: ")
print(onedarray)

print("- - -")

twodarray = np.array([[1,2,3,4],[5,6,7,8]])
print("NumPy",twodarray.ndim,"D Array: ")
print(twodarray)

print("- - -")

threedarray = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print("NumPy",threedarray.ndim,"D Array: ")
print(threedarray)

a = np.array(42) #0D
b = np.array([1,2,3,4,5]) #1D
c = np.array([[1,2,3,4],[5,6,7,8]]) #2D
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]]) #3D

print("- - -")

fivedarray = np.array([1,2,3,4], ndmin=5)
print("NumPy", fivedarray.ndim,"D Array: ")
print(fivedarray)

print("- - -")

print("Accessing Array Elements")
arr = np.array([1,2,3,4,5])
print("arr =",arr)
print(arr[0], "is the 1st element in the array")
print("This is a",arr.ndim,"D Array")

print("Adding arr[0] or",arr[0],"and arr[4] or",arr[4],"is",arr[0]+arr[4])

print("- - -")

print("Accessing 3D Arrays")
print(threedarray[0,1,2])

print("- - -")
print(c)
print("This is a",c.ndim,"D Array")
print("Last element from 1st dim:",c[0,-1])
print("Last element from 2nd dim:",c[1,-1])

print("- - -")

print("Array Slicing")

slicingarray = np.array([1,2,3,4,5,6,7,8])
print(slicingarray)
print(" ")
print("If I were to slice this array from its index 2 to index 6, I would get:")
print(slicingarray[1:5])
print(" ")
print("But if I were to slice from the index 4 to the end, I would get:")
print(slicingarray[4:])
print(" ")
print("And if I were to slice from the index 1 to the index 4, I would get:")
print(slicingarray[:4])

print("- - -")

print("Negative Slicing")
print("Using the same array as previously, we can also negatively slice.")
print(slicingarray)
print(" ")
print("Negative Slicing from 3rd index from end, to 1st index from end:")
print(slicingarray[-3:-1])

print("- - -")

print("Another array function is 'Step'")
print("Let's reuse the array from earlier:")
print(slicingarray)
print(" ")
print("Every other element from index 1 to index 5:")
print(slicingarray[1:5:2])
print(" ")
print("We can also get every other element from the entire array:")
print(slicingarray[::2])

print("- - -")

print("Slicing 2D Arrays")
print("Let's try slicing a 2D array we made earlier.")
print(c)
print(" ")
print("From the second element, slicing elements from index 1 to index 4:")
print(c[1,1:4])

print("- - -")