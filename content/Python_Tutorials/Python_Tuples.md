+++
Categories = ["Development", "Python", "USCL"]
Description = "Immutable Lists.."
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-10T02:01:53-04:00"
title = "Python_Tuples"

+++


<h1 align='center'>Python Tuples</h1>

Python tuple is much like a list except that it is immutable or unchangeable once created. Tuples use parentheses and creating them is as easy as putting different items separated by a comma between parentheses.
Example:


    tuple1 = ('Python', 'Julia', 1, 3.1415)
    type(tuple1)




    tuple



Pretty simple, so the next question is why do we need a new datatype? The answer can be summed up in three points:

Tuples are faster than lists. If you ever defined a set of constant values and all you ever want to do is read those values, you should use tuples instead of lists
Safer Code. Tuples are like 'write-protected' lists so that the data cannot be changed by accident.
Tuples are using in string formatting (we will see this in some examples below)
##Creating a Tuple

We already saw one example above on how to create tuples with multiple items but to create a tuple with a single item, you need to include a comma after the first item.
Example:


    tuple1 = ('Python',)

## Slicing the Tuple

Slicing a tuple is similar to slicing a list.
Example:


    tuple1 = ('Python', 'Julia', 1, 3.1415)
    tuple1[1:3]




    ('Julia', 1)




    tuple1[0::2]




    ('Python', 1)



From above example we can observe that just like lists, slicing a tuple returns a new shallow copied tuple containing the requested items.

## Tuple Concatentation, Repetition, Membership

Tuples are immutable objects which means that yo cannot update, append, remove, modify the items in the tuple. However what you can do is take items from different tuples and create new tuples with those. Let's take a look at some examples:


    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = ('a', 'b' , 'c' ,'d' , 'e')
    tuple1 + tuple2  # Tuple Concatentation




    (1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e')




    tuple1*2  # Tuple Repetition




    (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)




    'a' in tuple2  # Membership operator, returns true if member of tuple




    True



## Nested Tuples

It is also possible to create a tuple of tuples or tuple of lists. 
Example:


    list1 = ['Python', 'Julia', 1, 3.1415]
    list2 = [('a', 'b'), ('c', 'd')]  # List of tuples is possible too!
    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = tuple(list1 + list2)+ tuple1  # Concatenating the list and converting to tuple. Then adding two tuples and storing it in another tuple
    tuple2




    ('Python', 'Julia', 1, 3.1415, ('a', 'b'), ('c', 'd'), 1, 2, 3, 4, 5)



Remember, we cannot concatenate a list and a tuple so we concatenate two lists and convert the new list into tuple by using the tuple built-in function. Then we concatenate that to tuple1 and store the new tuple as tuple2.

## Traversing a Tuple

Tuples can be traversed using the index value of the items. The most straightforward way of traversing a tuple is by using loops.
Example: (extending the above example and using the items of tuple2)


    for i in enumerate(tuple2):
        print 'tuple2[{0[0]}]: {0[1]}'.format(i)

    tuple2[0]: Python
    tuple2[1]: Julia
    tuple2[2]: 1
    tuple2[3]: 3.1415
    tuple2[4]: ('a', 'b')
    tuple2[5]: ('c', 'd')
    tuple2[6]: 1
    tuple2[7]: 2
    tuple2[8]: 3
    tuple2[9]: 4
    tuple2[10]: 5


Woaah! Forget about tuples, what kind of sorcery is that in the print statement, right? Well it is one of the most wonderful built-in functions of python that you will come across. Let's keep the 'tuple' aside for a second. 
.format() is an extremely convenient way of formatting the text exactly the way we want it. It is available for python 2.7 and above (again, a gentle reminder to update your python is you're using python 2.6 or lower). What's wrong in our older % way of doing things right? Well, firstly, format method seems more sophisticated than using the %. Moreover % can take either a variable or a tuple or anything and throw bunch of errors for example lets say we have a tuple of two items..
Example:


    tuple1 = ('Python', 1)
    print 'Contents of tuple1: %s'%(tuple1)  # Will throw TypeError


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-8de7465d8254> in <module>()
          1 tuple1 = ('Python', 1)
    ----> 2 print 'Contents of tuple1: %s'%(tuple1)  # Will throw TypeError
    

    TypeError: not all arguments converted during string formatting



    print 'Contents of tuple1: {}'.format(tuple1)

    Contents of tuple1: ('Python', 1)



    print('This is {0}, and I rank {1} among all programming languages'.format(*tuple1))
    # The * helps in unpacking the tuple into arguments

    This is Python, and I rank 1 among all programming languages


That's all we will talk about format here, If you want to learn more about the format method, you can head over to [`official documentation`](docs.python.org/2/library/string.html#format-specification-mini-language 'Official Documentation'). format is a very handy tool for formatting individual values.

Coming back to our tuples, from the above examples, it must've made it very clear that almost everything that we did in lists apply over here. Ofcourse except for the fact that we can modify the lists items but not the tuples.

## Tuple Comprehension

We know that list comprehension is performed using a for loop that traverses the list and evaluates a condition using if.. else condition and creates a new list with the output. So for tuples it should be same as the list, right? Let's see:
Example:


    tuple1 = (1, 2, 3, 4, 5)
    tuple2 = (i for i in tuple1 if i%2 == 0)  # Same example as in list comprehension
    type(tuple2)




    generator




    tuple2.next()




    2



Remember when we talked about list comprehension and got all happy looking at such an easier way to create new lists? It so happens that the 'comprehension' for lists and dictionaries is just a syntactic sugar to use a generator expression that outputs a specific type. We learned basics about generators when we saw range and xrange in [`Python Loops`](newclasses.nyu.edu/access/lessonbuilder/item/13294871/group/9ce294e5-cc8b-44f8-963b-8160554a987f/Python%20Lab/Week%201/Python%20Loops/Python%20Loops 'Python Loops') List comprehension under the covers creates a generator expression that outputs a list (just like we did above using next() method). Now that you know the truth behind the comprehension you might feel that you don't need list comprehension but believe me, it is awfully handy for lists when you start writing your codes in python using lists. So if you want  to use comprehension in tuples, you will get a generator expression and you can obtain your results using the next method. This also doesn't require the invention of another brace or bracket.

## Built-in Tuple Functions and Methods

Python provides following methods for tuples:

### cmp(tuple1, tuple2):

The cmp method compares the elements of the two tuples. If the elements are of same type then perform simple comparison and return the result. If the elements are strings then sort them alphabetically and compare. If one of them has alphabets then that tuple is always greater (numbers are smaller than alphabets).
Example:


    tuple1 = ('a', 'b')
    tuple2 = (1, 2, 3)
    cmp(tuple1, tuple2)




    1



### len(tuple1):

len method returns the number of elements in the tuple.
Example:


    tuple1 = ('a', 'b')
    len(tuple1)




    2



### max(tuple1):

This method returns the elements from the tuple with the maximum value.
Example:


    tuple1 = ('a', '99999')
    max(tuple1)  # Remember alphabets are always greater than integers




    'a'



### min(tuple1):

This method returns minimum value of all the elements in the tuple.
Example: (extending the above example)


    min(tuple1)




    '99999'


