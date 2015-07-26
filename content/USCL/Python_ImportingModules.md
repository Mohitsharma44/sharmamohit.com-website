+++
Categories = ["Development", "Python", "USCL"]
Description = "Importing packages and modules in python"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-22T09:06:37-04:00"
title = "Python_ImportingModules"

+++


<h1 align='center'>Importing Modules and Packages</h1>

If you quit the ipython terminal or python interpreter, the functions and variables are lost. What if you want to access them in your other programs or at a later point of time?(You don't expect to complete your projects in a day do you?) Therefore you are better of using a text editor to prepare the input for the interpreter and running it with that file as input. This file is known as script. Now, you might have written several programs and some of them require a function that you wrote in a script for some other project. You want to use that handy function! There is no point in Ctrl+C and Ctrl+V for all these programs. To support this, python has a way to use these functions or definitions by using import.

## What is a Module?

A module is a python file that (generally) has only definitions of variables, functions and classes. It can also have executable statements if you'd like. A module allows you to logically organize your python code. Grouping related code in a module makes the code easier to understand and use. The module can have components that are imported from other modules.

## Import Statement

It is customary (and we have followed this in a couple of examples) to place all the import statements at the beginning of the module. Let's create a python file with functions that will perform addition, subtraction, multiplication and division of two numbers:


    # Create a file by name my_calc.py in your current directory and write this code:
    def mul(a ,b):
        return a * b
    
    def div(a, b):
        return a / b
    
    def add(a, b):
        return a + b
    
    def sub(a, b):
        return a - b

Now we shall import the file and just use the functions directly. Fire up your ipython terminals in the current directory.


    import my_calc  # Import our above module


    sum = my_calc.add(123, 456)  # Use add function


    print 'Sum = ',sum

    Sum =  579


You can use any python source file as a module by executing an import statement in some other python source file, just like we did. A module is loaded only once regardless of the number of times it is imported. So if you made any error in writing the file/ module that you are trying to import in ipython session, you will have to reload the module in the current ipython session.

When the python interpreter encounters an import statement it looks for the module name in the built-in modules first. if not found, it then searches for a file by the module's name in a list of directories that are given by variable PYTHONPATH (it is an environment variable which is basically a list of directory names) and it looks for the file in the current directory. If it fails everywhere then it goes and looks on the default path. On linux/ unix the default path is normally /usr/local/lib/python

## from .. import ..

To preserve your current namespace, python's from statement let's you import only specific attributes to your current namespace. Let's take a look at how this works. We will use our same my_calc.py file as a file that we are importing.




    from my_calc import div


    division = div (6, 7.)
    print 'Division = ',division

    Division =  0.857142857143



    # Let's print only upto 2 decimal places.. Remember how to do it?
    divison = div(6,7.)
    print 'Division = {0:.2f}'.format(divison)

    Division = 0.86


Using for statement does not import the entire file (or module) into the current namespace, it just introduced the item div from the module into our namespace. You might be wondering what if your file has many functions, you will go crazy writing so many import statements! Well.. it is also possible to import all names or definitions from a module into the current namespace by using for statement.


    from my_calc import *  # * means everything/ all


    division = div (6, 7.)


    print 'Division = ',division

    Division =  0.857142857143


--------
## Exercise

- Using python's built-in module sys, try to find the path for directories in which python will look for the modules. (Hint: Use Ipython and make use of tab completions and ? )


- Find a way to reload the module in the current ipython session.


- Find out the names or definitions that you have defined currently. Next, find the names or definitions of the module that you are trying to import. 
