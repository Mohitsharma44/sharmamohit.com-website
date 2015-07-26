+++
Categories = ["Development", "Python", "USCL"]
Description = "Handling Errors in Python"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-12T20:02:29-04:00"
title = "Python_ExceptionHandling"

+++


<h1 align='center'>Python Exception Handling</h1>

An exception is a python object that represents an error. It is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. When such a situation occurs and if python is not able to cope with it, it raises and exception. We have been seeing errors like TypeError and NameError or IndentationError throughout our tutorial which caused our application or that code to stop the execution. To prevent this from happening, we have to handle such exceptions.
Following is a hierarchy for built-in exceptions in python:


    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StandardError
          |    +-- BufferError
          |    +-- ArithmeticError
          |    |    +-- FloatingPointError
          |    |    +-- OverflowError
          |    |    +-- ZeroDivisionError
          |    +-- AssertionError
          |    +-- AttributeError
          |    +-- EnvironmentError
          |    |    +-- IOError
          |    |    +-- OSError
          |    |         +-- WindowsError (Windows)
          |    |         +-- VMSError (VMS)
          |    +-- EOFError
          |    +-- ImportError
          |    +-- LookupError
          |    |    +-- IndexError
          |    |    +-- KeyError
          |    +-- MemoryError
          |    +-- NameError
          |    |    +-- UnboundLocalError
          |    +-- ReferenceError
          |    +-- RuntimeError
          |    |    +-- NotImplementedError
          |    +-- SyntaxError
          |    |    +-- IndentationError
          |    |         +-- TabError
          |    +-- SystemError
          |    +-- TypeError
          |    +-- ValueError
          |         +-- UnicodeError
          |              +-- UnicodeDecodeError
          |              +-- UnicodeEncodeError
          |              +-- UnicodeTranslateError
          +-- Warning
               +-- DeprecationWarning
               +-- PendingDeprecationWarning
               +-- RuntimeWarning
               +-- SyntaxWarning
               +-- UserWarning
               +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning

Example:


    1 / 0


    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-1-b710d87c980c> in <module>()
    ----> 1 1 / 0
    

    ZeroDivisionError: integer division or modulo by zero


Quite straightforward example where we are trying to divide a number by 0. Python raises a ZeroDivisionError and the execution halts. There are basically two ways to handle this error. 
First way is to check and make sure that the divisor is not zero. This is left as an exercise for the students. The other way to handle the error is by using try.. catch block where we place the code to be executed inside the try block and the exception to be handled in the except block.
Example:


    for i in range(3, -3, -1):
        try:
            print 1.0 / i
        except ZeroDivisionError:
            print 'So, you\'re trying to divide by zero huh?'
            pass

    0.333333333333
    0.5
    1.0
    So, you're trying to divide by zero huh?
    -1.0
    -0.5


As observed from the above example, our execution continued even after we tried dividing 1.0 by zero.

## Argument of an Exception

An exception can have an argument, which is a value that gives additional information about the problem that caused the exception. The contents of argument vary by exception. You can capture an exception's argument by supplying a variable. Let's take a look at an example.
Example:


    for i in range(3, -3, -1):
        try:
            print 1.0 / i
        except ZeroDivisionError, e:
            print 'Zero Division Error: ',e
            pass

    0.333333333333
    0.5
    1.0
    Zero Division Error:  float division by zero
    -1.0
    -0.5


If you write the code to handle a single exception, you can have a variable following the exception in the except statement. This variable receives the value of the exception mostly containing the cause of the exception. If you are handling multiple exceptions, you can have a variable follow tuple of the execution. Based on whether you are handling single value or multiple exceptions, the variable can receive a single or multiple values in the form of a tuple.

## Hierarchy of Exceptions

The exceptions are organized in an hierarchy as observed from above tree. This means that we can have multiple exceptions handled by the except block.
Example:


    import time  # time module has a sleep method which will help slow down the execution of loop
    i = -2
    while i < 5:
        i = i + 1
        try:
            print 1.0 / i
            time.sleep(2)  # This will halt the code for 2 seconds
        except KeyboardInterrupt:
            # Lets raise the exception that we just caught!
            raise KeyboardInterrupt('Ctrl C pressed')
        except ZeroDivisionError:
            print 'So, you\'re trying to divide by zero huh?'
            pass

    -1.0
    So, you're trying to divide by zero huh?
    1.0
    0.5
    0.333333333333



    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    <ipython-input-4-66aad6d147e5> in <module>()
          8     except KeyboardInterrupt:
          9         # Lets raise the exception that we just caught!
    ---> 10         raise KeyboardInterrupt('Ctrl C pressed')
         11     except ZeroDivisionError:
         12         print 'So, you\'re trying to divide by zero huh?'


    KeyboardInterrupt: Ctrl C pressed


After starting the execution of the code, wait for few seconds and then press Cntrl+C on your keyboard and you should get the above error. The new thing that we can observe in this code is that we have used a keyword raise. This helps in raising a particular exception and as a parameter to the exception you can pass the string that you want to print. 

The raise statement does two things: it creates an exception object, and immediately leaves the expected program execution sequence to search the enclosing try statements for a matching except clause. The effect of raise statement is to either divert execution in a matching except suite, or to stop the program (if no proper exception handling was performed).

Now lets see the above example with hierarchy in action:


    import time
    i = -2
    while i < 5:
        i = i + 1
        try:
            print 1.0 / i
            time.sleep(2)  # This will halt the code for 2 seconds
        except BaseException:
            # Lets raise the exception that we just caught!
            print 'Some Exception occurred..'
            pass
        

    -1.0
    Some Exception occurred..
    1.0
    0.5
    Some Exception occurred..
    0.333333333333
    0.25
    0.2


In the above example we can see that we did implement a handler (a very bad kind, must say). If you check from the hierarchy list, you can observe that KeyboardInterrupt and ArithmeticError(which includes ZeroDivideError) are subclass of BaseException class. So since we implemented BaseException handler, all the errors under the base class are handled. Avoid raising a generic exception like we did in this example because you will not be able to understand what actually caused the exception and allows bugs to pass through. Instead use the most specific Exception constructor that semantically fits your issue.

## Finally

There is a finally keyword which is always executed regardless of where there was any exception in the code or not. This is generally used to cleanup some resources in a program.. especially when using file I/O operations
Example


    f = None
    try:
        f = open('test.txt', 'r')  # Open file in read-only mode
        f.readlines()  # Read all lines
    except IOError:
        print 'Error Opening File'
    finally:
        if f:  # If the file was opened
            f.close  # Close the file

In the above example we can observe that we are trying to open a file and read its contents. If the file doesn't exist, it will raise an IOError exception. We are handling that, no worries. However once the file has been read, we need to close the file so that other processes or other functions in our code can access it. (Remember: when accessing/ modifying a file, the file is locked to that process which is performing the I/O operation on it. Unless the lock is released, no other process will be able to modify it.. ) To make sure we release the resources, in the finally block we are checking if f is not null and closing it. 
