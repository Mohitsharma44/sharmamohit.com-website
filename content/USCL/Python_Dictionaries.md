+++
Categories = ["Development", "Python", "USCL"]
Description = "A container of Key-Value pairs"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-07-06T15:01:20-04:00"
title = "Python_Dictionaries"

+++


<h1 align='center'>Python Dictionaries</h1>

A dictionary is a container of key-value pairs. Just like lists, python dictionaries are mutable and can contain mixed types, however the key in the dictionary is immutable just like strings or numbers and are unique within a dictionary. Python dictionaries are also known as hash tables in other programming languages. Each key is separated from its value by a colon (:) and just like lists the items are separated by commas and thre whole thing is enclosed in curly braces. 
Example:


    student = {'Name': 'John', 'Class': 'Urban Skills', 'Course': 'Python'}
    student




    {'Class': 'Urban Skills', 'Course': 'Python', 'Name': 'John'}




    type(student)




    dict




    states = {}  # Creating empty dictionary


    states['AL'] = 'Alabama'  # Keys are inside square brackets and values on the right side of assignment


    states['NY'] = 'New York'


    states




    {'AL': 'Alabama', 'NY': 'New York'}



### fromkeys( )

The fromkeys() method creates a new dictionary from a list.
Example:


    states_list = ('AL', 'NY')
    states_dict = {}.fromkeys(states_list, 0)  # Instead of 0 you can leave the field empty
    states_dict['AL'] = 'Alabama'
    states_dict['NY'] = 'New York'
    states_dict




    {'AL': 'Alabama', 'NY': 'New York'}



## Accessing Dictionary Items:

There are various ways of accessing elements of dictionary. Best way to understand them are through the examples.
Example:


    student = {'Name': 'John', 'Class': 'Urban Skills', 'Course': 'Python'}
    student['Name']




    'John'




    student.get('Course', 'Not Found')  # If key is in Dictionary, it will return the value




    'Python'




    student.get('Location', 'Not Found')  # If key is not found, it will return second parameter of argument




    'Not Found'



## Updating Dictionary:

The dictionary can be updated by adding a new entry or a new key-value pair, modifying existing entry and/ or deleting an entry.


    student = {'Name': 'John', 'Class': 'Urban Skills', 'Course': 'Python'}
    student['Degree'] = 'Masters'
    student['Name'] = 'Tom'
    student




    {'Class': 'Urban Skills',
     'Course': 'Python',
     'Degree': 'Masters',
     'Name': 'Tom'}



As you must have observed, a new value to the dictionary can be added or modified simply by passing the key value pair to the dictionary. 

### setdefault( )

In python, the value (of a key-value pair) is mutable. However at times you might not want to overwrite the existing key-value pair but if it does not exist, you might want to add it. To perform this, you can use the setdefault() method. setdefault method returns a value if a key is present. Otherwise it inserts a key with the specified value and returns the value
Example:


    student = {'Name': 'John', 'Class': 'Urban Skills', 'Course': 'Python'}
    student.setdefault('Degree', 'Masters')  # This will add the 'Degree:Masters' key value pair to the dictionary since it doesn't exist





    'Masters'




    student.setdefault('Class','Urban Sensing')




    'Urban Skills'




    student




    {'Class': 'Urban Skills',
     'Course': 'Python',
     'Degree': 'Masters',
     'Name': 'John'}



### update( )

The update method adds (joins) the two dictionary together.
Example:


    states_dict = {'AL': 'Alabama', 'NY': 'New York'}
    states_dict2 = {'NJ': 'New Jersey', 'CA': 'California'}
    states_dict.update(states_dict2)
    states_dict




    {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}



## Removing from Dictionary

### pop( )

Pop() method removes the key-value pair based on the key passed as an argument. It returns the value that is being 'popped' from the dictionary
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    states_dict.pop('AL')




    'Alabama'




    states_dict




    {'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}



### del( )

del() method can be used to perform the above operation and also can be used to remove an entire dictionary. It does not return anything.
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    del states_dict['AL']
    states_dict




    {'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}




    del states_dict


    states_dict  # Will raise an error because we deleted the object.


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-20-0d583e464cf4> in <module>()
    ----> 1 states_dict  # Will raise an error because we deleted the object.
    

    NameError: name 'states_dict' is not defined


### clear( )

clear method clears all items from the dictionary


    states_dict = {'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    states_dict.clear()
    states_dict




    {}



## Traversing a Dictionary

### for loop:

A dictionary can be traversed by using for loops.
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    for k in states_dict:
        print k, states_dict[k]

    NY New York
    CA California
    NJ New Jersey
    AL Alabama



    for k, v in states_dict.items():  # We will see items() method in next sub- topic
        print ': '.join((k, v))

    NY: New York
    CA: California
    NJ: New Jersey
    AL: Alabama


### keys( ) , values( ) and items( )

The keys() method returns a list of keys in dictionary. The values() method returns a list of all the values and items() returns a list of all key-value tuples.
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    states_dict.keys()




    ['NY', 'CA', 'NJ', 'AL']




    states_dict.values()




    ['New York', 'California', 'New Jersey', 'Alabama']




    states_dict.items()




    [('NY', 'New York'),
     ('CA', 'California'),
     ('NJ', 'New Jersey'),
     ('AL', 'Alabama')]



## Sorting

Dictionaries in python can be sorted using keys or values. Just like keys the dictionaries can be sorted in ascending or descending order. First let us look as the built-in function sorted() and then the method specific to collections class.

### sorted( )

Sorted method returns a sorted list from the items in the iterable (in our case it is a dictionary). It can also take a boolean value for reverse which, if set as True, will sort the iterable in descending order. It is actually the most efficient way to sort anything, be it strings, integers, dictionaries, lists etc. 
Example:




    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    for key in sorted (states_dict.iterkeys()):
        print '%s : %s'%(key, states_dict[key])

    AL : Alabama
    CA : California
    NJ : New Jersey
    NY : New York



    for key in sorted (states_dict.iterkeys(), reverse=True):
        print '%s : %s'%(key, states_dict[key])

    NY : New York
    NJ : New Jersey
    CA : California
    AL : Alabama


If you observe the above example, we have used a function iterkeys() This function returns an iterator over the dictionary's keys..

### sort( )

Just like the sort method in lists, the method simply sorts the data. 
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    k = states_dict.keys()
    k.sort()  # For reverse sorting, pass the argument reverse=True
    for x in k:
        print '%s : %s'%((x, states_dict[x]))

    AL : Alabama
    CA : California
    NJ : New Jersey
    NY : New York



    

---------
## Exercise

- 1

 - An iterator, as the name suggests creates an iterator object which can be manually accessed using next() method. As an exercise, create a dictionary's keyiterator object and assign it to a variable and then access the items/ elements of the iterator object using next() method.

 - Use the built-in method iter() and see what is the output when you use next function with it.

 - Sort the items by their values.

## Views

The views are methods that are introduced in Python 2.7 (It is highly recommended to upgrade your python version if you are running Python version < 2.7) The problem with dictionary methods like items() is that it wastes the resources by creating a copy of the dictionary's key, value pair. However view() methods reflect the changes without creating a copy. Basically, views doesn't care if the dictionary has been changed, all it does is show the view of the dictionary. Let's take a look at an example that shows difference between iteritems() and viewitems().
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    s_iter = states_dict.iteritems()
    states_dict.pop('AL')




    'Alabama'




    for i in s_iter:
        print i


    ---------------------------------------------------------------------------

    RuntimeError                              Traceback (most recent call last)

    <ipython-input-31-e32cc735634f> in <module>()
    ----> 1 for i in s_iter:
          2     print i


    RuntimeError: dictionary changed size during iteration


We expected an error right? Because the iterator was trying to go through all the items in the dictionary and suddenly it detected that dictionary was changed due to our pop() method.
Now lets try the same thing with viewitems() instead of iteritems() and see if we still get an error or not.
Example:


    states_dict = {'AL': 'Alabama', 'CA': 'California', 'NJ': 'New Jersey', 'NY': 'New York'}
    s_view = states_dict.viewitems()
    s_view




    dict_items([('NY', 'New York'), ('CA', 'California'), ('NJ', 'New Jersey'), ('AL', 'Alabama')])




    states_dict.pop('AL')
    s_view  # We didn't modify it after popping.




    dict_items([('NY', 'New York'), ('CA', 'California'), ('NJ', 'New Jersey')])



This example makes it clear that viewitems does not create a copy, it just shows the current dictionary. If you try using items() method or iteritems() method after modifying the dictionary, it will always throw an error.

---------
## Exercise

Exercise: Try using the viewkeys() and viewvalues() and compare the differences between them and iteritems() & iterkeys().

*Remember, If you have any difficulty using any function or method in IPython, type the function or method name followed by a '?'. It will print the docstring/ help manual for you.*
