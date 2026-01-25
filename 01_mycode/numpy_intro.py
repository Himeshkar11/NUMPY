import numpy as np
# print(np.__version__)
# multipliying each elemnt in a list
my_list = [1,2,3,4]
my_list = my_list*2
print(my_list)
# to store the new updated list using new_list
new_list=[]
for item  in my_list:
    item = item *2
    new_list.append(item)
print(my_list)
print(new_list)
# creating a numpy array
# name_of_array = np.array(pass_a_list)
array = np.array([1,2,3,4])
print(array)
print(type(array)) # gives the type of array
# doubling the elements in a array
array = array*2
print(array)
# multi dimensional array
# each array can be classified into the following types
# to check the dimension of an array we use the function .ndim which tells number of dimensions 
# 1. zero dimension array 
# here only a single charcater or number i9s passed into the array arguemnt 
arr0d = np.array('A')
print(arr0d)
print(arr0d.ndim)
# 2. one dimensional array 
# here only a single list is passed as an argument to the array of numpy 
arr1d = np.array(['A','B','C','D'])
print(arr1d)
print(arr1d.ndim)
# 3. two dimensional matrices
# her list are created inside list to stimulate a matix of order n with n rows andn columns 
arr2d = np.array([['a','b','c'],
                 ['d','e','f'],
                 ['g','h','i']])
print(arr2d)
print(arr2d.ndim)
# 4. three dimnesional array 
# here the 3d array is formed as array([[[a],[b],[c]]]) where a , b and c are their own lists 
arr3d = np.array([ [ ['a','b','c'],['d','e','f'],['g','h','i'] ],
                  [ ['j','k','l'],['m','n','o'],['p','q','r'] ],
                  [ ['s','t','u'],['v','w','x'],['y','z',''] ]])
print(arr3d)
print(arr3d.ndim)
print(arr3d.shape)

# accesing the elements
# 1. earlier in lists way
print(arr3d[0][0][0]) # a
# 2. numpy way
print(arr3d[0,0,0])# b

# print ass by the words above using indexing
word =arr3d[0,0,0] +arr3d[2,0,0] +arr3d[2,0,0]
print(word)

word2 = arr3d[0,0,1] + arr3d[1,1,2] + arr3d[0,0,2] + arr3d[0,2,1]+arr3d[1,1,2]
print(word2)

# slicing in numpy
# slicing in numpy is same as slicing in string and is done according to the index with start end and step values denoted by a colon
print("row slcing")
arr = np.array([ [1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
print(arr[0:4],"\n")
print(arr[1:4],"\n")
print(arr[0:3],"\n")
print(arr[2:],"\n")
print(arr[:],"\n")
print(arr[::-1],"\n")
print(arr[0:4:2],"\n")
print(arr[::-2],"\n")
print("column slicing")
# same principle as row slicing
# print(arr[,0]) to print the first elemnt at column of all the rows we use : before comma
print(arr[:,0],"\n") # 1 5 9 13
print(arr[:,0:4],"\n")
print(arr[:,1:4],"\n")
print(arr[:,0:3],"\n")
print(arr[:,2:],"\n")
print(arr[:,:],"\n")
print(arr[:,::-1],"\n")
print(arr[:,0:4:2],"\n")
print(arr[:,::-2],"\n")

print("both row and column slicing")
arc = np.array([ [1,2,3,4],
                 [5,6,7,8],
                 [9,10,11,12],
                 [13,14,15,16]])
print("quadrant 1")
print(arc[0:2,0:2],'\n')
print("quadrant 2")
print(arc[0:2,2:],"\n")
print("quadrant 3")
print(arc[2:,0:2],'\n')
print("quadrant 4")
print(arc[2:,2:],'\n')

# arithmetic
# scaler arithmetic
print("scaler arithmetic of a array")
arrsc = np.array([1,2,3])
print(f"addition arithemtic : {arrsc +1} \n")
print(f"subtraction arithemtic : {arrsc -2}\n")
print(f"multiplicaion arithemtic : {arrsc *3}\n")
print(f"division arithemtic : {arrsc /4}\n")
print(f"power arithemtic : {arrsc **5}\n")

print("vectorized arithmetic of a array")
print(f"these are functions which can be appiled to an 1 d array.")
print(f"square root function \n syntax : np.sqrt(array) \n square root of array arrsc is {np.sqrt(arrsc)}")

arrvec = np.array([1.01,2.50,3.99])
print("the rounding of of the above array can be done using three functions \n",
      " 1. round \n syntax : np.round(array) \n ",
      f" example {np.round(arrvec)}",
      "function : rounds of  the number acc to mathematical rules \n ",
      "2. floor \n syntax: n[.floor(array) \n",
      f" example {np.floor(arrvec)}",
      " function : always bring the number down  \n",
      " 3. ciel \n syntax : np.ciel(array) \n ",
      "function : always increases the decimal",
      f" example {np.ceil(arrvec)}")
print("chittti question ")
print("given below is the array of radii of three circles \n return the array of the areas of the three circles corresponding to their radii")
radii = np.array([1,2,3])
print(f"the array of the areas coressponding to their radii is : {np.pi *(radii**2)}")

print("element wise arithmetic ")
print("here the operation between two arrays gives a new array whose elemnta are the operated elemnts of the two arrays ")
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
print(f"the two arays are {array1} and {array2}")
print(f"addition of arrays {array1 + array2}")
print(f"subtraction of arays {array1 - array2}")
print(f"multiplication of arays {array1 * array2}")
print(f"divison of arrays {array1 / array2}")
print(f"power of arrays {array1 ** array2}")
print("comparision operators")
print("these are operators which return a boolean array by comparing the condition with each elemnt of the array")
scores = np.array([99,45,100,89,60])
print(f"this is the boolean array for this condition scores == 100 {scores == 100}")
print(f"this is the boolean array for the condition of pass marks socres>=60 {scores>=60}")
print(f"this is the boolean array of all the failed students scores <60 {scores<60}")
print("we can also use this in assignment operators where upon achieveing the condition we can change the value of that cases")
scores[scores<60]= 0
print(f"this is the aray in which those who scored less than 60 marks will be termed with zero marks {scores}")