import numpy as np
import pyscreenshot as ss

# l = [1,2,3,4,5]
#
# a = np.array(l)
#
# print(a)
# print(a)
#
# print(type(a))
#
#

#
# l = []
#
# for i in range(0,4):
#     int_i = int(input("Enter value  : "))
#     l.append(int_i)
#
# a = np.array(l)
#
# print(a)
# print(a.ndim)
# b = np.array([[1,2,3],[4,5,6]])
#
# print(b)
# print(b.ndim)

# ---Array filled with 0's(using zeros function) -------
#
# zero = np.zeros(3)
# print()
# zero1 = np.zeros((4,4))
# print(zero)
# print()
# print(zero1)

# ----------Array filled with 1's(using once function) ------

# ones = np.ones(4)
# ones1 = np.ones((4,4))
#
# print(ones)
# print()
# print(ones1)


# -----Empty Array -----------

# ar_empty = np.empty(4)
# print(ar_empty)    # prints random values or past execution values that have been stored in memory


#-------Full Array ------------

# a = np.full((3,3),7)
# print(a)


# ---------Array with a range of elements------------

# ar_range = np.arange(4)
# print(ar_range)

# Program to take screenshot


# To capture the screen

# image = ss.grab()
#
# image.show()
# image.save("123.jpeg")

# ----------Diagnal Array filled with 1's------------

# ar_dia = np.eye(3)
# print(ar_dia)
# print()
# arr_dia = np.eye(5,5)
# print(arr_dia)

# ------------Array with values that are spaced linearly in a specified interval-------------


# arr_lin = np.linspace(0,20,num=5)
#
# print(arr_lin)

# --------eye()--------

# a = np.eye(3,3,k = 0)
# print(a)


# ---------Random valued arrays--------


# ------rand() function to print random valued array(values will be between 0 to 1)


# ran_arr = np.random.rand(5)
# print(ran_arr)
#
# random_arr = np.random.rand(3,3)
# print(random_arr)

# ------randn() function to print random valued array(values will be close to 0 and it could be positive or negative)

# randn_arr = np.random.randn(4,4)
# print(randn_arr)

# ------ranf() function to print random valued array(values will be between 0 to 1(1 not included))
#
# arr = np.random.ranf((3,4))
# print(arr)

# ------randint(min,max,Array_size) function to print random valued array(values will be between given range)

# arr = np.random.randint(5,20,(4,5))
# print(arr)


# Data Types in Numpy

# get data types using dtype func

# var = np.array([1, 2, 3, 4, 5])
# print("Data Type : ", var.dtype)
#
# # changing data type
#
# a = np.array([1, 2, 3, 4, 5], dtype=np.int8)
# print(a)
# print("Data type: ", a.dtype)
# print()
#
# # changing data type using function
#
# b = np.float32(a)
# print(b)
# print("Data type: ", b.dtype)
# print()
# new = np.int_(b)
# print(new)
# print(new.dtype)
# print()
#
#
# # using astype()

# print(a)
# print("Data type : ",a.dtype)
# print()
# new_1 = a.astype(float)
#
# print(new_1)
# print("Data Type : ",new_1.dtype )

# -----Shape and Reshaping in numpy array----------

#
# a = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
# print(a)
# print(a.shape)
# #
# b = np.array([1, 2, 3, 4], ndmin=4)                 # ndmin to assign how many dimensional array it is
# print(b)
# print(b.ndim)
# print(b.shape)


#------Reshaping------------reshape(rows,cols,dimensions)

# a = np.array([1,2,3,4,5,6])
# print(a)
# print("Shape of array : ",a.shape)
# print("Dimension of array : ",a.ndim)
# print()
# b = a.reshape(3,2)
# print(b)
# print("Shape of array : ",b.shape)
# print("Dimension of array : ",b.ndim)



# a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(a)
# print("Shape of array : ",a.shape)
# print("Dimension of array : ",a.ndim)
# print()
# b = a.reshape(2,3,2)                #reshape(outermost will have 3 arrays, in that there will be 3 araays and each will have 2 elements)
# print(b)
# print("Shape of array : ",b.shape)
# print("Dimension of array : ",b.ndim)
# #
# c = b.reshape(-1)
# print(c)
# print("Shape of array : ",c.shape)
# print("Dimension of array : ",c.ndim)






# -------------Numpy_Arithmetic Operations-----------

# -----1D Array----

# addition
#
# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# varadd = var1 + 3
# var_add = var1 + var2

#using arithmetic function

# varadd = np.add(var1,3)
# var_add = np.add(var1,var2)
# print("Array 1 : ",var1)
# print("Array 2 : ",var2)
# print()
# print("Addition of Array 1 with 3 : ",varadd)
# print()
# print("Addition of Array 1 and Array 2 : ",var_add)
#

#subtraction

# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# varadd = var1 - 1
# var_add = var1 - var2

#using arithmetic function

# varadd = np.subtract(var1,1)
# var_add = np.subtract(var1,var2)

# print("Array 1 : ",var1)
# print("Array 2 : ",var2)
# print()
# print("Subtraction of Array 1 with 1 : ",varadd)
# print()
# print("Subtraction of Array 1 and Array 2 : ",var_add)
#


# multiplication

# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# # varadd = var1*2
# # var_add = var1 * var2
#
# #using arithmetic function
#
# varadd = np.multiply(var1,2)
# var_add = np.multiply(var1,var2)

# print("Array 1 : ",var1)
# print("Array 2 : ",var2)
# print()
# print("Multiplication of Array 1 with 2 : ",varadd)
# print()
# print("Multiplication of Array 1 and Array 2 : ",var_add)
#


#Division

# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# # varadd = var1/2
# # var_add = var1 / var2
#
# #using arithmetic function
#
# varadd = np.divide(var1,2)
# var_add = np.divide(var1,var2)
#
# print("Array 1 : ",var1)
# print("Array 2 : ",var2)
# print()
# print("Division of Array 1 with 2 : ",varadd)
# print()
# print("Division of Array 1 and Array 2 : ",var_add)



# mod

# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# # varadd = var1 % 3
# # var_add = var1 % var2
#
# #using arithmetic function
#
# varadd = np.mod(var1,2)
# var_add = np.mod(var1,var2)
#
# print("Array 1 : ",var1)
# print("Array 2 : ",var2)
# print()
# print("Modulo of Array 1 with 2 : ",varadd)
# print()
# print("Modulo of Array 1 and Array 2 : ",var_add)
#


# power



# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# # varadd = var1**2
# # var_add = var1 ** var2
#
# #using arithmetic function
#
# varadd = np.power(var1,2)
# var_add = np.power(var1,var2)
#
# print("Array 1 : ",var1)
# print("Array 2 : ",var2)
# print()
# print("Power of Array 1 with 2 : ",varadd)
# print()
# print("Power of Array 1 and Array 2 : ",var_add)
#

# ----2D Array------

#Addition
#
#
# var1 = np.array([[1,2,3,4],[4,2,1,3]])
# var2 = np.array([[3,2,1,4],[1,2,3,4]])
# var_add = var1 + var2
# print(var1)
# print()
# print(var2)
# print()
# print(var_add)


#Multiplication

#
# var1 = np.array([[1,2,3,4],[4,2,1,3]])
# var2 = np.array([[3,2,1,4],[1,2,3,4]])
# var_add = var1 * var2
# print(var1)
# print()
# print(var2)
# print()
# print(var_add)


#Reciprocal = 1/x
#
# var1 = np.array([1,2,3,4])
# var2 = np.array([1,2,3,4])
# res = np.reciprocal(var1)
#
# print(res)


# Arithmetic Functions

# var1 = np.array([1,2,3,4,6,23,4,32,8])
#
# # For 2D Array
#
# var2 = np.array([[1,2,3,4],[3,6,4,3]])
# print("max in column(axis = 0) : ",np.max(var2,axis=0))
# print("max in row(axis = 1) : ",np.max(var2,axis=1))

# print()

# For 1D Array


# max= np.max(var1)
# print("Maximum value : ",max)
# print()
# print("Minimum value : ",var1.min())
# print()
# print("Position index of maximum number is : ",var1.argmax())
# print()
# print("Position index of minimum number is : ",var1.argmin())
# print()
# print("Square root of element 4 : ",np.sqrt(4))
# print()
# print("Sin values of var1 Array : ",np.sin(var1))
# print()
# print("COs value of 90",np.cos(90))
# print()
# print("cumsum value for Array var1 : ",np.cumsum(var1))





# ----Broadcasting------

#
# var = np.array([1,2,3])
# var1 = np.array([[1],[2],[3]])
# print(var)
# print()
# print(var1)
#
# print("Addition : \n",np.add(var,var1))




#-------Indexing and Slicing-------

# #1D Array
#
# var = np.array([5,7,6,9])
# print("Dimension : ",var.ndim)
# print(var[2])
#
# # 2D Array
#
# var1 = np.array([[4,6,5],[7,8,9]])
# print("Dimension : ",var1.ndim)
# print(var1[1,2])
#
# # 3D Array
#
# var2 = np.array([[[1,2],[2,3]],[[2,6],[5,9]]])
# print("Dimension : ",var2.ndim)
# print(var2[1][1][1])


# -------Slicing------

# 1D Array

# print()
# var = np.array([1,2,3,4,5,6,7])
#
# print("Whole Array : ",var)
#
# print()
#
# print("Sliced Array from 2 to 5 : ",var[1:5])
# print()
# print("Sliced Array from 2 to end of array : ",var[1:])
# print()
# print("Sliced Array from start to 5 : ",var[:6])
# print()
# print("Whole Array with step value of 2 : ",var[::2])
# print()
# print(" Array with starting from 2 to 6 step value of 2 : ",var[1:7:2])
#
#
# #2D Array
#
# var = np.array([[1,2,3,4,5,6,7],[2,5,8,3,9,2,1]])
#
# print(var[1,1:5])



# -----------Iterating Array-------

# 1D Array
#
# x = np.array([1,2,3,4,5])
# print(x)
# print()
#
# for i in x:
#     print(i)

# 2D Array

# x = np.array([[1,2,3,4,5,6],[6,5,4,3,2,1]])
#
# print(x)
# print()
#
# for i in x:
#     for j in i:
#         print(j)


# 3D Array

# x = np.array([[[1,2,3,4],[6,7,8,9]]])
# print(x)
# print()
# print(x.ndim)
# print()
#
# for i in x:
#     for j in i:
#         for k in j:
#             print(k)


# iterating without using nested for loops(Using nditer() function )
#
# x = np.array([[[1,2,3,4],[6,7,8,9]]])
#
# print(x)
# print()
#
# for i in np.nditer(x):
#     print(i)


# to change data type of iterated elements


# x = np.array([[[1,2,3,4],[6,7,8,9]]])
#
# print(x)
# print()
#
# for i in np.nditer(x,flags=['buffered'],op_dtypes="S"):
#     print(i)


# to print iteration with indexing

# x = np.array([[[1,2,3,4],[6,7,8,9]]])
# print(x)
# print()
# print(x.ndim)
# print()
#
# for i,d in np.ndenumerate(x):
#     print(i,d)



# copy vs view
#
# a = np.array([1,2,3,4])
#
#
# co = a.copy()
#
# #if you make any changes in original it doesn't reflect in copied array as copy function makes another array
#
# a[1] = 23
#
# print("a : ",a)
# print()
#
#
# print("copy : ",co)
#
# print()
# b = np.array([1,2,3,4,5])
# vi = b.view()
#
# # if you make any changes in original it will reflect in copied array as view function has no data it is the same original array
#
# b[2] = 21
# print("b : ",b)
# print()
# print("view : ",vi)



# ---Join Array-----

#1D Array
#
# x = np.array([1,2,3,4,5])
# y = np.array([6,7,8,9,0])
# #
# con = np.concatenate((x,y))
# print(con)
#
# stack = np.stack((x,y),axis=1)
# print(stack)

# 2D Array

#
# x = np.array([[1,2,3,4,5],[0,9,8,7,6]])
# y = np.array([[6,7,8,9,0],[5,4,3,2,1]])
#
# con = np.concatenate((x,y),axis=1)
#
# print(x)
# print()
# print(y)
# print()
# print(con)
#
# stk = np.stack((x,y),axis=1)
# stk1 = np.hstack((x,y))      # joins arrays in Columns(horizontal)
# stk2 = np.vstack((x,y))      # joins arrays in rows(verticle)
# stk3 = np.dstack((x,y))      # joins array height-wise
# print(stk)
# print()
# print(stk1)
# print()
# print(stk2)
# print()
# print(stk3)
# print()
#

# ---Split-------

# # 1D Array
#
# x = np.array([1,2,3,4,5])
# y = np.array([6,7,8,9,0])
#
# print(x)
# print()
# z = np.array_split(x,3)        # np.array_split(array_name,number of arrays you want after split)
# print(z)
# print(z[0])
#
# #2D Array
#
# x = np.array([[1,2,3,4,5],[0,9,8,7,6]])
# y = np.array([[6,7,8,9,0],[5,4,3,2,1]])
#
# print(x)
# print()
#
# z = np.array_split(x,3,axis=0)        # np.array_split(array_name,number of arrays you want after split)
#
# print()
# print(z)
# print()
# print(z[0])
#



# Search using where( araay_name == element ) function      returns an array of index number where searched element is
#
# a = np.array([1,2,3,42,5,3,2,7,6,4,5])
#
# s = np.where(a==2)
# print(s)

# b = np.array([2,3,4,5,6,7,8,9,1])
#
# s = np.where((b%2)==0)
# print(s)

# search index value where I can insert any specific element using searchsorted() function

# a = np.array([1,2,3,4,8,9])
#
# x = np.searchsorted(a , 5)
# print(x)
#
# y = np.searchsorted(a, [5,6,7,9],side="right")
# print(y)


# Sorting using sort() function
#
# a = np.array([[1,7,5],[2,8,4],[3,9,0]])
#
# sort = np.sort(a)
# print(sort)
#
# b = np.array(["a", "p","t","e","x"])
# print(np.sort(b))
#


# Filter Array

# b = np.array(["a", "p","t","e","x"])
#
# f = [True,False,True,False,True]
#
# filtered_array = b[f]
# print(filtered_array)
# print(type(filtered_array))



#---------Arithmetic Functions----------


# Shuffle() function

# a = np.array([1,2,3,4,5])
#
# np.random.shuffle(a)            #shuffle arranged element from an array
# print(a)


# unique() function

# a = np.array([1,2,3,4,2,5,2,6,2,7])
#
# x = np.unique(a,return_index=True,return_counts=True)            # filtered array for only unique data and removes repeating data
# print(x)


# Resize() function

# a = np.array([1,2,3,4,5,6,7,8,9,0])
#
# b = np.resize(a, (3,3))
# print(b)
#

# Flatten & Ravel

# a = np.array([1,4,2,6,3,7])
# b = np.resize(a,(2,3))
# print(b)
# print()
#
# print("Flatten : ",b.flatten(order="C"))                  #order = "c" means to flatten in row-major (C-style) order.
# print()
# print("Flatten : ",b.flatten(order="F"))                  #‘F’ means to flatten in column-major (Fortran- style) order
# print()
# print("Flatten : ",b.flatten(order="K"))                   #‘A’ means to flatten in column-major order if a is Fortran contiguous in memory, row-major order otherwise.
# print()
# print("Flatten : ",b.flatten(order="A"))                  #‘K’ means to flatten a in the order the elements occur in memory. The default is ‘C’.
# print()
#
# print("Ravel : ",np.ravel(b,order="F"))                   #Ravel uses same order as flatten
#



# ---------Insert Function--------


# a = np.array([1,2,3,4,5,6,7])
#
# print(a)
# print(type(a))
# print()
# v = np.insert(a,(1,3),33)               #insert(array_name, position, value)----can use multiple positions----can't use float values
# print(v)


#2D Array
#
# a = np.array([[1,2,3,4],[5,6,7,8]])
#
#
# print("for column : ")
# print()
# v1 = np.insert(a, 2, [23,24,5,7],axis=0)   #axis=0 == column
# print(v1)
# print()
# print("For row : ")
# print()
# v2 = np.insert(a, 2, [23,45],axis=1)   #axis=1 == row
# print(v2)

# v2 = np.append(a,[[23,12,43,56]],axis=0)
# print(v2)

#-------------Delete--------------

# a = np.array([1,2,3,4,5,6,7])
#
# print(a)
# print()
# d = np.delete(a,3)
# print(d)




# ---------Matrix--------

# a = np.matrix([[1,2,3],[4,5,6]])
# b = np.matrix([[1,2,3],[4,5,6]])
#
# print(a)
# print()
# print(b)
# print()
# print("sum : \n", a+b)


# a = np.matrix([[1,2,3],[4,5,6]])
# b = np.matrix([[1,2,3],[4,5,6]])
#
# print("Subtractiom : \n",a-b)
#
#
# a = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
# b = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
#
# print(" multiplication : \n",a.dot(b))        matrix uses dot() function to multiply



#------Matrix Functions-----------

# Transpose

# a = np.matrix([[1,2],[3,4],[5,6]])
# #
# print(a)
# print()
# # print("Trnspose of a : \n", np.transpose(a))              #using transpose() function
# print()
# print("OR")
# print()
# print("Trnspose of a : \n", a.T)                        # Using short method which is  : (array_name.T)


# Swapaxes

# a = np.matrix([[1,2],[3,4],[5,6]])
# print(a)
# print()
# print("Swapped axes of a : \n", np.swapaxes(a,0,1))              #using swapaxes(array_name, from_axes, To_axes) function


# Inverse matrix

# a = np.matrix([[1,2],[3,4]])
# print(a)
# print()
# print("inverse matrix : \n",np.linalg.inv(a))

# Power


# a = np.matrix([[1,2],[3,4]])

# print(a)
# print()
# print("A to the power 2 : \n",np.linalg.matrix_power(a,2))
# print()
# print("A to the power 0 : \n",np.linalg.matrix_power(a,0))
# print()
# print("A to the power -2 : \n",np.linalg.matrix_power(a,-3))


#-------------Determinate-----------


# a = np.matrix([[1,2],[3,4]])
#
# print("Determinate of a matrix : \n ",np.linalg.det(a))
#
# b = np.matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(b)
#
# print("Determinate of b matrix : \n ",np.linalg.det(b))


#-----------Copy NumPy array into another array--------

#using empty_like()


# importing Numpy package
# import numpy as np
#
# # Creating a numpy array using np.array()
# ary = np.array([13, 99, 100, 34, 65, 11,
# 				66, 81, 632, 44])
#
# print("Original array: ")
#
# # printing the Numpy array
# print(ary)
#
# # Creating an empty Numpy array similar
# # to ary
# copy = np.empty_like(ary)
#
# print("copy : \n",copy)
# # Now assign ary to copy
# copy[:] = ary
#
# print("\nCopy of the given array: ")
#
# # printing the copied array
# print(copy)

# using copy()


# ary = np.array([13, 99, 100, 34, 65, 11,
# 				66, 81, 632, 44])
#
# print("Original array: ")
#
# print(ary)
#
# copy = np.copy(ary)
#
# print("\nCopy of the given array: ")
#
# # printing the copied array
# print(copy)



# using assignment operator


# ary = np.array([13, 99, 100, 34, 65, 11,
# 				66, 81, 632, 44])
#
# print("Original array: ")
#
# print(ary)
#
# copy1 = ary
#
# ary[4] = 78
#
# print("\nCopy of the given array: ")
#
# # printing the copied array
# print(copy1)



# ------------swap columns of a given NumPy array---------------

#
# my_array = np.arange(12).reshape(4, 3)
# print("Original array:")
# print(my_array)
#
# my_array[:, [2, 0]] = my_array[:, [0, 2]]
# print("After swapping arrays the last column and first column:")
# print(my_array)


# -------Insert new axis to the array---

# using numpy.newaxis() function

#
# arr = np.arange(5*5).reshape(5, 5)
# print(arr.shape)
#
# # promoting 2D array to a 5D array
# # arr[None, ..., None, None]
# arr_5D = arr[np.newaxis, ..., np.newaxis, np.newaxis]
#
# print(arr_5D.shape)


# using np.expand_dims() function

# x = np.zeros((3, 4))
#
# print(x)
# print()
# y = np.expand_dims(x, axis=1)
# print(y)
# print()
# print("shape of y : ",y.shape)


arr = np.arange(5*5).reshape(5,5)
print(arr)
print()
print(arr.shape)

newaxes = (0, 3, -1)
arr_5D = np.expand_dims(arr, axis=2)
print(arr_5D)
print()
print(arr_5D.shape)
