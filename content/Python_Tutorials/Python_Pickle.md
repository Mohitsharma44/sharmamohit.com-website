+++
Categories = ["Development", "Python", "USCL"]
Description = "Serializing and Storing of data while preserving its data structure"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-29T00:07:47-04:00"
title = "Python_Pickle"

+++


<h1 align='center'>Python Pickle</h1>

Pickle module implements an algorithm for turning your Python object into a series of bytes by the process of serialization. Before we can jump into the unique feature of pickling, lets understand what serialization means.

Serialization is the process of converting a data structure or object state into a format that can be stored and resurrected later in the same or another computer environment. During resurrection, when the series of bytes is reread according to the serialization algorithm, it can be used to create a semantically identical clone of the original object. This process of serializing an object is also called as deflating an object. The opposite operation, as you must've guessed, is called inflating. You can read more about serialization on [`wikipedia`](https://en.wikipedia.org/wiki/Serialization 'Serialization').

In python, the bulk of pickle module is written in C. It can store arbitrary complex python data structures however since it stores python objects, it is very highly unsafe as it can contain malicious data. So remember, pickle is good if only you create your pickle file locally and do not share it with some one. 

Now lets see some of the datatypes that pickle can store:

- All the native datatypes that python supports such as booleans, integers, complex numbers, strings etc 
- Collections such as lists, tuples, dictionaries containing any combination of native datatypes.
- Lists, Dictionaries and Tuples containing Nested combinations of ...... you get it!
- Methods, Functions, Classes, Instances etc.

## Constructing Pickle data:

Lets jump directly into code and I will explain as we go.


    student = {}
    student['name'] = 'Jack'
    student['course'] = 'Urban Skills Lab'
    student['enrolled'] = True
    student['misc'] = ('full-time', )

In the above example, we have created a student dictionary. Now lets save the above dictionary to a pickle file

## Saving data as Pickle:


    import pickle
    try:
        with open('test_pickle.pkl', 'wb') as f:
            pickle.dump(student, f)
    except IOError, e:
        print 'IOError: ',e

Did you check out a new way to open file object for writing? With this technique, you don't have to worry about closing the file_object. As soon as the while loop is broken, the file_object will automatically be closed. (Think why?)
Ok, so the dump() method in pickle module takes the serializable python data structure, serializes it into a binary and save it to the file. Now lets try loading the data. To make sure it works, lets open an new ipython terminal or just close your current session and reopen it fresh.

## Loading Data from Pickle file


    import pickle
    try:
        with open('test_pickle.pkl', 'rb') as f:
            s = pickle.load(f)
    except IOError, e:
        print 'IOError: ',e
    
    s





    {'course': 'Urban Skills Lab',
     'enrolled': True,
     'misc': ('full-time',),
     'name': 'Jack'}



And voila! a new data structure is created with the data structure that is equal to the original data structure.

This technique only works when you are working in python. If you want this to be compatible with other programming languages then you will have to take a look at other serialization format like JSON. 
This is beyond the scope of the subject and is left as a self-assignment for interested students.
