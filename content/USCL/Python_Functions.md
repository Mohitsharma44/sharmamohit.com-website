+++
Categories = ["Development", "Python", "USCL"]
Description = "A block of organized and reusable code that can be used to perform single, related action."
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-17T20:02:58-04:00"
title = "Python_Functions"

+++


<h1 align='center'>Python Functions</h1>

Imagine that you have to open a file, read the contents of the file and close it. Pretty trivial, right? We did that in the exception handling. Now imagine that you have to read ten files, print their output and close it. Now you don't want to sit there and type file i/o operations for every file. what if there are over 50 files and you have to concatenate them to a single file? This is where the functions come in. A function is a block of organized and reusable code in a program that performs a specific task which can be incorporated into a larger program. The advantages of using functions are:

- Reuse of code
- Reducing duplication of the code
- Improving readability and reducing complexity of the code

There are two basic types of functions: Built-in functions and user defined functions. We have been using built-in functions for quite some time without actually understanding how a function works. This is the beauty of python. According to Guido van Rossum, all objects in python are first class citizens. Meaning all the objects (like function, strings, integers etc) have equal status. That is they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments and so forth. We have been doing this the whole time, right? Now lets see how you can create your own functions and call them in your code.

## Defining Functions

A function is defined using the def keyword followed by the name of the function. The parameters or the arguments should be placed within the parentheses followed by the function name. The code block within every function starts with a colon and should be indented.

From here on, I might ask you to write the piece of code using your favorite text editor and execute the code. 
Example:


    # Create test_func.py file and write the following code
    '''
    Author = Mohit
    Date = June 20, 2014
    This is our first script with user-defined functions
    '''
    def mul(a, b):  # defining a function
        print a,'*',b,'=',a * b
    
    def info():  # defining a function
        return __doc__
    
    print info()
    mul(4, 5)

    
    Author = Mohit
    Date = June 20, 2014
    This is our first script with user-defined functions
    
    4 * 5 = 20


Save the above file and execute it: python test_func.py and you should get an output that looks like above.

In the above code we have used a keyword return.  A function may or may not have a return value. The job of return is just to return the expression/ object to the the calling function. 

-------
## Exercise

Try to execute this code. If there is an error, what do you think caused it? Try rectifying the error.

`Create test_func.py file and write the following code`


    '''
    Author = Mohit
    Date = June 20, 2014
    This is our first script with user-defined functions
    '''
    
    def mul(a, b):
        print info()  # Calling a function from another function
        print a,'*',b,'=',a * b
    
    def info():
        return __doc__

## Calling a function

Defining a function only gives it a name, specifies the parameters and structures the blocks of code but unless you call the function, the function is never executed. Just like above example, once the basic structure of a function is finalized, the function can be called by just using the function name followed by the arguments/ parameters enclosed in parenthesis. You can also call the function from another function. There are two ways of passing the parameters to the functions.

### Pass by Reference

All the parameters in the python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. Let's take a look at an example:




    def append_list(list1):
        list1.append(99)


    l1 = [1, 2, 3, 4, 5]
    append_list(l1)
    l1




    [1, 2, 3, 4, 5, 99]



Here we are maintaining reference of the passed object and appending values to the same object thus modifying the actual object.

## Pass by Value


    def remove_list(list1):
        del(list1)
        list1 = [21, 22, 23, 24, 25]


    l1 = [1, 2, 3, 4, 5]
    remove_list(l1)
    l1




    [1, 2, 3, 4, 5]



From the above example we can observe that the parameter list1 is local to the function and modifying the list1 does not affect l1. The function basically accomplishes nothing. 

## Function Arguments

A function can be called by using following types of formal arguments

- Required arguments
- Keyword arguments
- Default arguments
- Variable-length arguments

### Required Arguments:

Required arguments are passed to a function in correct positional order. The number of arguments being passed should be equal to the number or arguments expected by the function that is defined. Let's take a look at the example:
Example:




    # Lame example
    def info(name, sem):
        print 'My name is: ',name
        print 'This is semester',int(sem)


    info('Mohit', '2')

    My name is:  Mohit
    This is semester 2



    info(2, 'Mohit')

    My name is:  2
    This is semester


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    <ipython-input-8-f692458a13af> in <module>()
    ----> 1 info(2, 'Mohit')
    

    <ipython-input-6-32fe472dcf83> in info(name, sem)
          2 def info(name, sem):
          3     print 'My name is: ',name
    ----> 4     print 'This is semester',int(sem)
    

    ValueError: invalid literal for int() with base 10: 'Mohit'


###  Keyword Arguments:

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name. This allows you to skip the arguments or place them out of order because python's interpreter will be able to match the values with parameters. Let's modify the way we are calling the above function.
Example:


    def info(name, sem):
        print 'My name is: ',name
        print 'This is semester',int(sem)

    



    info(sem = 2,  name = 'Mohit')  # The order of the parameter does not matter.

    My name is:  Mohit
    This is semester 2


### Default Arguments:

A default argument is an argument that assumes a default value if the value is not provided when the function is called. Let's modify the above example and specify sem = 2 by default.
Example:


    def info(name, sem = 2):  # Default argument for semester is 2
        print 'My name is: ',name
        print 'This is semester',int(sem)


    info('Mohit', 2)

    My name is:  Mohit
    This is semester 2



    info('Jack')  # Not providing second argument.

    My name is:  Jack
    This is semester 2


### Variable Length Arguments: 

At some point, you may need to process the function for more than the arguments that you specified when you defined the function. These arguments can be of variable length and are not named in the function definition, unlike required and default arguments. So how do you handle this? Let's take a look at another example:
Example:


    def names(course, *names):
        print 'Name of course: ',course
        print 'Name of students in the course:'
        for name in names:
            print name


    names('Python', 'Jim', 'Jack', 'Mat')

    Name of course:  Python
    Name of students in the course:
    Jim
    Jack
    Mat


An asterisk (*) is placed before the variable name that holds the values of all non keyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. 

## Anonymous Functions

Anonymous functions do not have a name! They are not declared in the standard manner using the def keyword. To create an anonymous function you can use lambda keyword. They are part of the functional paradigm incorporated in python.

- Lambda forms can take any number of arguments but they return just one value in the form of an expression. They cannot contain commands or multiple expressions. 
- Lambda functions have their own local namespace (just like regular functions) and cannot access variables other than those in their parameter list or those in the global namespace.
- Lambda function cannot be a direct call to print function.
Example:




    mul = lambda a, b: a*b


    print mul(4, 5)

    20

