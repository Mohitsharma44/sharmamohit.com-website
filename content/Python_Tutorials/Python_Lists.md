+++
Categories = ["Development", "Python", "USCL"]
Description = "One of the most basic data structure in Python"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-05T02:00:44-04:00"
title = "Python_Lists"

+++


<h1 align='center'>Python Lists</h1>

Last week we studied Python Strings and we saw that Python's most basic data structure is the sequence. Each element of a sequence is assigned a number known as index number. List is one of the most commonly used sequence of the seven built-in sequences in Python. (The others are: str, unicode, tuple, bytearray, buffer, xrange. We have already discussed str and unicode last week in Python Strings). Just like str, you can do a lot of things with these sequences ranging from indexing, slicing, adding, checking for membership, length of sequence etc. just like we saw with the strings.

The list is the most versatile datatype available in Python which can be written as a list of comma-separated values between square brackets. Creating a list is as simple as putting different items separated by comma between square brackets.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a




    ['Python', 'Julia', 1, 3.1415]




    type(a)




    list




    a[2]




    1



Python is zero-index based, thus to get the first item we simply ask for the item/ element on the 0th index. We will now briefly go over the basic list manipulations (which are similar to strings) and then look at some more methods that makes lists unique.

## Slicing the List

A shallow copy of the list is performed and a new list is created containing the requested elements.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a[:2]  # Performs shallow copy and returns new list with first two elements




    ['Python', 'Julia']



The slicing can also  be done to get the n-th value from a list by passing n as the third argument.


    a = ['Python', 'Julia', 1, 3.1415]
    a[1::2]  # Take every second element from index value 1.




    ['Julia', 3.1415]




    a[-3:-2:1]  # Take every element between index value -3 and -2
    # Remember, it doesn't include the nth index value when traversing a list.




    ['Julia']



## Updating the List

Unlike strings and tuples which are immutable, elements in list can be changed without having to create a new list, thus making it mutable.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a[2] = 'Java'
    print '\nArray: \n',a
    print '\nLength of array: \n',len(a)

    
    Array: 
    ['Python', 'Julia', 'Java', 3.1415]
    
    Length of array: 
    4



    a[2:4] = []  # Remove some elements/ changing the size


    print '\nArray: \n',a
    print '\nLength of array: \n',len(a)

    
    Array: 
    ['Python', 'Julia']
    
    Length of array: 
    2


## Appending to the List

New items can be easily added to the list by using the append() method.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.append('C++')  # It will append the item to the end of the list
    a




    ['Python', 'Julia', 1, 3.1415, 'C++']



## Copying Lists

There are many ways to create a copy of the lists in python. Lets take a look at few techniques:

### copy package

copy packages is packaged with the python so you don't have to install it externally to use it. So what is the reason of creating a separate package? From our first week's session on variables, we know that it is very easy to create copy of objects,right? We do know one thing for sure that assignment statements ( '=' ) in python do not copy the objects, they merely create bindings between the target and the object, right? It so happens that for collections that are mutable or contains mutable items, a copy is sometimes needed so that one can change the content of the mutable item without changing the other. There are actually two ways of creating a copy of an object viz: shallow copy and deep copy. In shallow copy, python constructs a new object and then inserts references to into it that are found in the original list, whereas deepcopy, as you must've guessed it, creates an object and copies everything. (If you are curious to know more about it, head over the [`official documentation`](https://docs.python.org/2/library/copy.html 'Python Copy Official Documentation') )


    import copy
    a = ['Python', 'Julia', 1, 3.1415]
    a1 = copy.copy(a)  # Shallow copy.. Fast
    a2 = copy.deepcopy(a)  # Deep copy.. Slower

### Slice Syntax


    a = ['Python', 'Julia', 1, 3.1415]
    a1 = a[:]
    print a1

    ['Python', 'Julia', 1, 3.1415]


### list method


    a = ['Python', 'Julia', 1, 3.1415]
    a1 = list(a) # when list method takes a list as a parameter, it creates a copy of that list 
    print a1

    ['Python', 'Julia', 1, 3.1415]


## Delete List Elements

To remove the list elements, one has two options to either use del statement or lists's remove method ( will be discussed later ).
Example:


    a = [1, 2, 3, 4, 5]
    a




    [1, 2, 3, 4, 5]




    del(a[4])
    a




    [1, 2, 3, 4]



## Nested Lists

It is also possible to create a list of the lists.
Example:


    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c', 'd', 'e']
    c = [a,b]
    c




    [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd', 'e']]



## List Concatenation, Repetition, Membership:

These are simple list manipulation methods similar to strings. Take a look at following example:


    a = [1, 2, 3, 4, 5]
    b = ['a', 'b', 'c', 'd', 'e']
    a + b  # List Concatenation




    [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']




    a * 2  # List Repition




    [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]




    3 in a  # Membership operator, returns true if member of list




    True



## Traversing a list:

The most straightforward way to traverse a list is using loops:

### for loop:
Example:


    a = [1, 2, 3, 4, 5]
    for i in a:
        print i

    1
    2
    3
    4
    5


Lets traverse using the index numbers:
Example:


    for i in range(len(a)): # start from 0 and go till the length of the list.
        print a[i]

    1
    2
    3
    4
    5


### While loop:

Just like for loop, we can traverse the list based on its index numbers:
Example:


    i = 0
    while i < len(a):  # till i is less than length of list
        print a[i]
        i += 1  # increment i by 1 at every iteration

    1
    2
    3
    4
    5


### enumerate( )

Python has a built-in method called enumerate which returns both index value and value of list ( or any other iterable object).
Example:


    for ind, val in enumerate(a):
        print 'a[%d] = %d'%(ind, val)

    a[0] = 1
    a[1] = 2
    a[2] = 3
    a[3] = 4
    a[4] = 5


## List Comprehension

List comprehension is a syntactic way of creating a list based on the existing list, just like we did in copying the lists above. 
The basic structure of the syntax includes a for loop that traverses the list and evaluates a condition using if.. else condition and stores the output of the condition as a new list. Lets take a look at a quick example.
Example:


    b = [i for i in a if i % 2 == 0]
    b




    [2, 4]



What we did in the line 2 is simply create a list b from the list items in a which are completely divisible by 2. 
There are many ways in which the list comprehension can be used. It is just a shorthand of writing better readable code.

## Built- in List Functions and Methods:

Python provides following methods for lists:

### cmp (list1 , list2): 

Compares elements between two lists. If the elements in lists are numbers, then performs numeric coercion if necessary and the compares the list1 against list 2. if it is found to be small then -1 is returned, else 1. If we reached the end of one of the lists, the longer list is "larger." If we exhaust both lists and share the same data, the result is a tie, meaning that 0 is returned.
If the elements in the list are alphabets then they are sorted alphabetically and first element is compared and the result is returned as explained for numbers.
Example:


    a = [1, 2, 3]
    b = [4, 1, 2]
    cmp(a , b)  # a is smaller than b




    -1



### max:

This method returns the elements from the list with maximum value.
Example:


    a = [1, 2, 3]
    max(a)
    ## What do you think will happen if we compare a list of the lists (nested list)?




    3



### min:

This method returns the element from the list with minimum value.

### list:

This method takes sequence types and converts them to lists. This is also used to convert a tuple to list.
Example:


    a = list(('Python', 'Julia', 1, 3.1415))  # iterable as a tuple
    a




    ['Python', 'Julia', 1, 3.1415]




    type(a)




    list



The first line might confuse a little. Lets understand it. list is a built-in function which can either create an empty list if it is called with no parameters, or create a new list of the iterable/ sequence that it is given as an input. That means that list can at most 1 argument. Thus we have to put our elements in a circular bracket (which makes it a tuple) and then pass it as a argument to list method. 

### list.count(obj):

This method returns the number of times the object, that is passed as a parameter, occurs in the list.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.count('Python')




    1



### list.extend(seq):

This method appends the contents of a sequence to a list.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    b = ['C++', 'Java', 2, 2.7182]
    a.extend(b)
    a




    ['Python', 'Julia', 1, 3.1415, 'C++', 'Java', 2, 2.7182]



### list.index(obj):

This method returns the lowest index in the list that object appears.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.index('Python')




    0



### list.insert(index, obj):

This method is used to insert the object at the offset index.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.insert(3, 2.7182)
    a




    ['Python', 'Julia', 1, 2.7182, 3.1415]



### list.pop(obj = list[-1]):

This method removes and returns the last object from the list.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.pop(3)




    3.1415



### list.remove(obj):

This method is used to remove the object from the list. Unlike pop, this does not return anything.
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.remove(1)


    a




    ['Python', 'Julia', 3.1415]



### list.reverse():

This method reverses the objects of list in place
Example:


    a = ['Python', 'Julia', 1, 3.1415]
    a.reverse()
    a




    [3.1415, 1, 'Julia', 'Python']



### list.sort([func]):

This method sorts objects of list by using the compare function passed as optional parameter. You can also sort the string in reverse by passing the optional parameter reverse=True
Example:



    a = ['Python', 'Julia', 1, 3.1415]
    a.sort()
    a




    [1, 3.1415, 'Julia', 'Python']




    a.sort(reverse=True)
    a




    ['Python', 'Julia', 3.1415, 1]



## Performance Characteristics:

The list has following performance characteristics:



- The list object stores pointers to objects, not the actual objects themselves. The size of a list in memory depends on the number of objects in the list, not the size of the objects.
- The time needed to get or set an individual item is constant, no matter what the size of the list is (also known as “O(1)” behaviour).
- The time needed to append an item to the list is “amortized constant”; whenever the list needs to allocate more memory, it allocates room for a few items more than it actually needs, to avoid having to reallocate on each call (this assumes that the memory allocator is fast; for huge lists, the allocation overhead may push the behaviour towards O(n\*n)).
- The time needed to insert an item depends on the size of the list, or more exactly, how many items that are to the right of the inserted item (O(n)). In other words, inserting items at the end is fast, but inserting items at the beginning can be relatively slow, if the list is large.
- The time needed to remove an item is about the same as the time needed to insert an item at the same location; removing items at the end is fast, removing items at the beginning is slow.
- The time needed to reverse a list is proportional to the list size (O(n)).
- The time needed to sort a list varies; the worst case is O(n log n), but typical cases are often a lot better than that.
