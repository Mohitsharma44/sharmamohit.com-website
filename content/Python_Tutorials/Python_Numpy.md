+++
Categories = ["Development", "Python", "USCL"]
Description = "Numerical processing library for scientific computing in Python"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-07-06T21:10:08-04:00"
title = "Python_Numpy"

+++


<h1 align='center'>Numpy</h1>

NumPy (Numerical Python) is an opensource library for scientific computing in python. Numpy let's you work with arrays and matrices in a natural way unlike lists where you have to loop through individual elements to perform any numerical operation.The methods in numpy are designed with high performance in mind. Numpy arrays are stored more efficiently than an equivalent data structure in python such as lists and arrays. This especially pays off when you are using really large arrays (large data sets). Major portion of numpy is written in C and thus the computations are faster than the pure python code. Numpy actually used to be a part of major scientific package called SciPy but eventually numpy was separated and now scipy uses numpy for its major tasks. 
So Let's jump into NumPy!

##Basics

Numpy's main object is the homogeneous multidimensional array. Numpy's array class is called ndarray. It is a table of numbers, indexed by a tuple of positive integers. In numpy dimensions are called as axes. The number of axes is known as rank. Arrays in numpy are similar to lists in Python except that numpy has an added requirement that all the elements must be numbers (obviously, its NumPy!). Lets look at how to create numpy arrays:
Example:


    import numpy as np
    a = np.array([1, 2, 3, 4], float)  # Single dimensional Array
    print 'Type: ',type(a)
    print 'Shape: ',a.shape
    print 'Dimension: ',a.ndim
    print 'Itemsize: ',a.itemsize
    print 'Size: ',a.size

    Type:  <type 'numpy.ndarray'>
    Shape:  (4,)
    Dimension:  1
    Itemsize:  8
    Size:  4


The method array, takes two arguments: the list to be converted into the array and the datatype of **every** member of the list. There are many attributes of ndarray and by now you should be able to understand how to access those attributes and get help for them. In the above example, I have mentioned a few more important ones. Let's understand what they mean.

###ndarray.ndim

It is the number of axes or dimensions of the array.

###ndarray.shape

It is the dimension of the array. This is a tuple of integers indicating the size of the array in each dimension. For matrix with n rows and m columns, the shape will be (m, n). The length of the shape tuple is therefore the rank, or number of dimensions, ndim

###ndarray.dtype

It is an object describing the type of the elements in the array. Remember that all the elements need to be of same datatype in a numpy array. Additionally numpy provides its own numpy.int16, numpy.int32, numpy.float64 and so on.

###ndarray.itemsize

The size in bytes of each element of the array. For example an array of elements of type float64 (above example) has itemsize of 64 / 8 = 64. While one complex32 has item size of 4 32 / 8. 

###ndarray.data

This is the buffer containing the actual elements of the array. Normally this attribute is not used as numpy offers many fancy indexing facilities.

##Numpy Datatypes

Numpy supports a much greater variety of numerical types than Python does.

|Data type	|Description|
|----------:|----------:|
|bool\_	|Boolean (True or False) stored as a byte
|int\_	|Default integer type (same as C long; normally either int64 or int32)
|intc	|Identical to C int (normally int32 or int64)
|intp	|Integer used for indexing (same as C ssize_t; normally either int32 or int64)
|int8	|Byte (-128 to 127)
|int16	|Integer (-32768 to 32767)
|int32	|Integer (-2147483648 to 2147483647)
|int64	|Integer (-9223372036854775808 to 9223372036854775807)
|uint8	|Unsigned integer (0 to 255)
|uint16	|Unsigned integer (0 to 65535)
|uint32	|Unsigned integer (0 to 4294967295)
|uint64	|Unsigned integer (0 to 18446744073709551615)
|float\_	|Shorthand for float64.
|float16	|Half precision float: sign bit, 5 bits exponent, 10 bits mantissa
|float32	|Single precision float: sign bit, 8 bits exponent, 23 bits mantissa
|float64	|Double precision float: sign bit, 11 bits exponent, 52 bits mantissa
|complex\_	|Shorthand for complex128.
|complex64	|Complex number, represented by two 32-bit floats (real and imaginary components)
|complex128	|Complex number, represented by two 64-bit floats (real and imaginary components)

Try using these dataypes in your codes and see the difference

##Array Creation

There are many ways in which an array can be created, we just saw one in our example above. Let's look at some other ways of creating arrays.
Example:


    a = np.arange(5, dtype=float)
    print '\n arange() with float dtype: \n',a
    b = np.arange(1, 6, 2, dtype=int)
    print '\n arange() with int dtype: \n',b  # \n will print new line
    c = np.ones((2, 3), dtype=float)
    print '\n ones(): \n',c
    d = np.zeros((2,3), dtype=float)
    print '\n zeros(): \n',d
    e = np.empty((2, 4))
    print '\n Empty: \n',e  # Your output might be different..
    f = np.ones_like(a)
    print '\n Ones_like(): \n',f
    g = np.diag(a)
    print '\n Diagonal array: \n',g

    
     arange() with float dtype: 
    [ 0.  1.  2.  3.  4.]
    
     arange() with int dtype: 
    [1 3 5]
    
     ones(): 
    [[ 1.  1.  1.]
     [ 1.  1.  1.]]
    
     zeros(): 
    [[ 0.  0.  0.]
     [ 0.  0.  0.]]
    
     Empty: 
    [[ -3.10503618e+231   1.73059848e-077   2.24228410e-314   6.93536013e-310]
     [  6.93536013e-310   2.92966904e-033   7.42620323e-091   7.26604178e-043]]
    
     Ones_like(): 
    [ 1.  1.  1.  1.  1.]
    
     Diagonal array: 
    [[ 0.  0.  0.  0.  0.]
     [ 0.  1.  0.  0.  0.]
     [ 0.  0.  2.  0.  0.]
     [ 0.  0.  0.  3.  0.]
     [ 0.  0.  0.  0.  4.]]


###np.arange()

is the same as the range function that we used previously.

###np.zeros() and np.ones()

as the name suggests, generate new arrays of specified dimensions filled with these values. These are most commonly used functions to create new arrays.

###np.empty()

This function creates an array whose initial content is random and depends on the state of the memory. If not specified, the data type of the created array is float64

###np.ones_like()  , np.zeros_like() and np.empty_like()

These functions create a new array with the same dimensions and type as the existing one but with the values as either ones or zeros or random value.

###np.diag()

As the name suggests, this will construct a diagonal array


##Printing Arrays

As you must have observed from the above examples, Numpy displays the arrays in a similar way to nested lists but with the following layout:

the last axis is printed from left to right
the second to last axis is printed from top to bottom.
the rest rest are also printed from top to bottom with each slice separated from the next by an empty line
Simply put, single dimensional array are printed as rows, bi dimensional and multi-dimensional are printed as matrices and as lists of matrices respectively. The examples will make it more clear.
Example:


    print '\nSingle Dimensional: \n',np.arange(4)
    print '\nTwo Dimensional: \n',np.arange(6).reshape(2,3) # We will talk about reshape soon..!
    print '\nThree Dimensional: \n',np.arange(12).reshape(2,3,2)

    
    Single Dimensional: 
    [0 1 2 3]
    
    Two Dimensional: 
    [[0 1 2]
     [3 4 5]]
    
    Three Dimensional: 
    [[[ 0  1]
      [ 2  3]
      [ 4  5]]
    
     [[ 6  7]
      [ 8  9]
      [10 11]]]


Selecting elements from an array is a trivial process. Just like lists, we can obtain the elements of the array by using their index value. Give it a shot! We will talk in detail about indexing later.


##Array Mathematics

When standard mathematical operations are used with numpy arrays, they are applied on an element-by-element basis and a new array is created and filled with the result. This means that the arrays should be of same size when any mathematical operation is performed on them. Lets take a look at some examples:
Example:


    a = np.array([1, 2, 3, 4])
    b = np.linspace(4, 16, num=4)
    
    print '\nb - a: \n', b-a
    b = np.linspace(4, 16, num=3)
    
    print '\nb - a: \n', b-a

    
    b - a: 
    [  3.   6.   9.  12.]
    
    b - a: 



    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-4-ec209d90aeb7> in <module>()
          5 b = np.linspace(4, 16, num=3)
          6 
    ----> 7 print '\nb - a: \n', b-a
    

    ValueError: operands could not be broadcast together with shapes (3,) (4,) 


Lets now see these operations on multi-dimensional arrays


    a = np.arange(4).reshape(2,2)
    print '\na: \n',a
    b = np.ones_like(a) * 2
    print '\nb: \n',b
    print '\na * b: \n',a * b  # This will perform element-wise multiplication
    print '\nDot Product: \n',np.dot(a, b)

    
    a: 
    [[0 1]
     [2 3]]
    
    b: 
    [[2 2]
     [2 2]]
    
    a * b: 
    [[0 2]
     [4 6]]
    
    Dot Product: 
    [[ 2  2]
     [10 10]]


The above operations have been performed on the two arrays with same datatype and so the result will have the same datatype as the operand arrays. However when you perform any operation on arrays with different datatypes, the type of the resulting array will correspond to the more general or precise one. This is also known as upcasting.


    a = np.ones(5, dtype='int16')
    b = np.linspace(3, 9, num=5)
    print '\nDtype of a: \n', a.dtype
    print '\nDtype of b: \n', b.dtype
    c = a + b
    print '\nC: \n',c
    print '\nDtype of c: \n',c.dtype

    
    Dtype of a: 
    int16
    
    Dtype of b: 
    float64
    
    C: 
    [  4.    5.5   7.    8.5  10. ]
    
    Dtype of c: 
    float64


Many Unary operations, such as computing sum of the elements in the array or finding the element in the array that has the maximum value are implemented as methods of ndarray class.

By default, these operations apply to the array as though it was a list of numbers, regardless of its shape. However by specifying the axis parameter you can apply an operation along the specified axis of an array.


    a = np.random.random((4, 4))
    print '\na: \n',a
    print '\nSum: \n',np.sum(a)
    print '\nMinimum: \n',np.min(a)
    print '\nMaximum: \n',np.max(a)
    print '\nMinimum at axis=0: ',a.min(axis=0)
    print '\nCumulative sum along each row: \n',a.cumsum(axis=1)

    
    a: 
    [[ 0.03393196  0.60967045  0.48575961  0.80389461]
     [ 0.45666937  0.1340573   0.77085133  0.1260247 ]
     [ 0.6278121   0.59825426  0.78261101  0.61532053]
     [ 0.3189249   0.01292406  0.2571509   0.79722091]]
    
    Sum: 
    7.43107798457
    
    Minimum: 
    0.0129240585016
    
    Maximum: 
    0.803894606649
    
    Minimum at axis=0:  [ 0.03393196  0.01292406  0.2571509   0.1260247 ]
    
    Cumulative sum along each row: 
    [[ 0.03393196  0.64360241  1.12936202  1.93325662]
     [ 0.45666937  0.59072667  1.361578    1.4876027 ]
     [ 0.6278121   1.22606636  2.00867737  2.6239979 ]
     [ 0.3189249   0.33184896  0.58899986  1.38622077]]


## Universal Functions
Numpy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called as ufunc (for universal functions). 


    a = np.linspace(0, 1, num=4)
    print '\nSin values: \n',np.sin(a)
    print '\nSquare Root of values: \n',np.sqrt(a)

    
    Sin values: 
    [ 0.          0.3271947   0.6183698   0.84147098]
    
    Square Root of values: 
    [ 0.          0.57735027  0.81649658  1.        ]


##Slicing
Slicing extracts the portion of a sequence by specifying a lower and upper bound. The lower bound element is included, but the upper-bound element is not included in slicing. Just like lists, there is a third parameter step which means the strides to be taken between the elements. Let's take a look at an example.


    a = np.linspace(5, 40, num=5)
    print '\nElements at index 0, 1, 2:\n',a[:3]
    # Just like lists, even negative indexing works:
    print '\nElements at index 0, 2, 4:\n',a[-5:5:2]

    
    Elements at index 0, 1, 2:
    [  5.    13.75  22.5 ]
    
    Elements at index 0, 2, 4:
    [  5.   22.5  40. ]


For multidimensional array, you specify in rows, columns format.


    a = np.linspace(5, 40, num=8).reshape(2,4)
    print '\nfirst row and second column: \n',a[1,2]
    print '\n All elements from second column: \n',a[:,2]

    
    first row and second column: 
    35.0
    
     All elements from second column: 
    [ 15.  35.]


Slices are references to memory in the original array. Changing the values in a slice also changes the original array


    a = np.arange(5)
    b = a[3:5]  # last two elements of a
    print '\nBefore changing b[0], b[0]: \n',b[0]
    b[0] = 99  # Indirectly changing second last element of a too!
    print '\nAfter changing b[0], a: \n',a

    
    Before changing b[0], b[0]: 
    3
    
    After changing b[0], a: 
    [ 0  1  2 99  4]


## Fancy Indexing
Numpy offers more indexing facilities than regular Python sequences. In addition to indexing by integers and slices, as we saw before, arrays can be indexed by arrays of integers and arrays of booleans

###Indexing with Arrays of Indices


    ind = None
    ind1 = None
    a = np.arange(12)**2
    print '\nArray a: \n',a
    # Taking array of indices:
    ind = np.random.random_integers(2, 10, size=(10,))
    print '\nIndices: \n',ind
    print '\nArray of elements at pos ind: \n',a[ind]
    ind1 = np.random.random_integers(2, 8, size=(3,4))
    print '\nIndices1: \n',ind1
    print '\nArray of elements at pos ind1: \n',a[ind1]

    
    Array a: 
    [  0   1   4   9  16  25  36  49  64  81 100 121]
    
    Indices: 
    [10  9  9  7  6  3  4 10  4  9]
    
    Array of elements at pos ind: 
    [100  81  81  49  36   9  16 100  16  81]
    
    Indices1: 
    [[7 4 4 8]
     [2 6 8 7]
     [3 7 3 2]]
    
    Array of elements at pos ind1: 
    [[49 16 16 64]
     [ 4 36 64 49]
     [ 9 49  9  4]]


When the indexed array is multidimensional, a single array of indices refers to the first dimension of a. Though we can provide indexes for more than one dimension, the indices for each dimension must have the same shape. The following example will make it much clear.


    a = np.arange(20).reshape(4,5)
    print '\nArray: \n',a
    ind1 = np.arange(4).reshape(2,2)
    print '\nIndex1: \n',ind1
    ind2 = np.random.random_integers(1, 5, size=(2,2))
    print '\nIndex2: \n',ind2
    # Remember ind1 and ind2 should be of same shape
    print '\na[ind1, ind2]: \n',a[ind1, ind2]
    print '\na[:,ind2]: \n',a[:,ind2]

    
    Array: 
    [[ 0  1  2  3  4]
     [ 5  6  7  8  9]
     [10 11 12 13 14]
     [15 16 17 18 19]]
    
    Index1: 
    [[0 1]
     [2 3]]
    
    Index2: 
    [[3 3]
     [1 1]]
    
    a[ind1, ind2]: 
    [[ 3  8]
     [11 16]]
    
    a[:,ind2]: 
    [[[ 3  3]
      [ 1  1]]
    
     [[ 8  8]
      [ 6  6]]
    
     [[13 13]
      [11 11]]
    
     [[18 18]
      [16 16]]]


Indexing with arrays is also used in search for the maximum value of time-dependent series. Lets take a look at an example:


    t = np.linspace(10, 150, 7) # create fake timescale
    data = np.sin(np.arange(25)).reshape(5,5) # Generate fake data
    ind = data.argmax(axis=0)
    max_t = t[ind]
    max_data = data[ind, xrange(data.shape[1])]
    print '\nMaximum Time: \n',max_t
    print '\nData at that maximum time: \n',data.max(axis=0)

    
    Maximum Time: 
    [ 103.33333333   10.           10.           33.33333333   56.66666667]
    
    Data at that maximum time: 
    [ 0.91294525  0.84147098  0.90929743  0.98935825  0.99060736]


We can also use indexing with arrays as a target to assign to.


    a = np.arange(10)
    a[[1, 3, 5, 9]] = 0
    print '\na: \n',a

    
    a: 
    [0 0 2 0 4 0 6 7 8 0]


###Indexing with Boolean Arrays
When we index arrays with arrays of indices, we aare providing a list of indices. With boolean indices, we explicitly chose the items in the array that we want and the one's we dont. Lets take a look at a quick example:


    a = np.arange(16).reshape(2,2,4)
    # Now lets select the indices whose value is greater than lets say 10
    b = a > 10
    print '\nElements with values > 10: \n',a[b]

    
    Elements with values > 10: 
    [11 12 13 14 15]


These come in very handy when we are working with things like thresholding where we can assign all values greater than the threshold be 0 or set them to threshold value.

## Tricks

### Automatic Reshaping
To change the dimensions of an array, you can omit one of the sizes which will then be deduced automatically:


    a = np.arange(30)
    a.shape = 2,-1,3  # -1 means "whatever is needed"
    a.shape




    (2, 5, 3)




    a




    array([[[ 0,  1,  2],
            [ 3,  4,  5],
            [ 6,  7,  8],
            [ 9, 10, 11],
            [12, 13, 14]],
    
           [[15, 16, 17],
            [18, 19, 20],
            [21, 22, 23],
            [24, 25, 26],
            [27, 28, 29]]])



### Vector Stacking

How do we construct a 2D array from a list of equally-sized row vectors? In MATLAB this is quite easy: if x and y are two vectors of the same length you only need do m=[x;y]. In NumPy this works via the functions column_stack, dstack, hstack and vstack, depending on the dimension in which the stacking is to be done. For example:


    x = np.arange(0,10,2)  # x=([0,2,4,6,8])
    y = np.arange(5)  # y=([0,1,2,3,4])
    m = np.vstack([x,y])
    xy = np.hstack([x,y])


    m




    array([[0, 2, 4, 6, 8],
           [0, 1, 2, 3, 4]])




    xy




    array([0, 2, 4, 6, 8, 0, 1, 2, 3, 4])



--------
#### I would also encourage you to check out some *[`numpy examples`]('http://wiki.scipy.org/Numpy_Example_List_With_Doc' "Numpy Examples")*
