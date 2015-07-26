+++
Categories = ["Development", "Python", "USCL"]
Description = "Introdution to Python Variables and detailed explanation on how they differ from variables in other OOP languages"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-05-28T21:56:15-04:00"
title = "Python_Variables"

+++


<h1 align='center'>Python Variables</h1>

As the name implies, a variable is something which can change. A variable is just a way of referring to a memory location used by a python program. Consider a variable as a container to store certain values. Based on the datatype of the variable, the python interpreter allocates the memory and decides what can be stored in the reserved memory. This will be a rather short chapter.


## Assigning Values to Variables:

One of the main differences between Python and strongly types languages like C++ or Java is the way it deals with the data types. In languages like C++ or Java, every variable must have a unique data type i.e if a variable is of type string it cannot store integers or floats. Moreover every variable has to be declared before it can be used, thus binding it to the data type that can be stored in it. Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when a value is assigned to a variable. This means that a variable that was used to store a string can now be used to store an integer. Try it out. Do something like this:


    s = 'I am in NYC'  # s is a string
    print s

    I am in NYC



    type(s)




    str




    s = 24  # Now s is an integer
    print s

    24



    type(s)




    int



> Did you see the type function that we used? Type is a built-in function that returns the datatype of anything.. and by anything, I mean absolutely anything (give it a spin!). It is one of the cool things in Python. We will talk about this and many other cool built-in functions in the later chapters. 

Every language has some rules for naming the identifier of variables (the variable name). In Python, a valid identifier is a non-empty sequence of characters of any length with:

The start of the character can be an underscore "\_" or a capital or lower case letter. However it is generally recommended to use all upper case for global variables and all lower case for local variables.
The letters following the first letter can be a digit or a string.
Python is a case-sensitive language. Therefore, name is not equal to Name.
Python keywords cannot be used at identifier names (Keywords in Python are reserved words that cannot be used as ordinary identifiers. 

||||||
|:-------|:--------|:---------|:--------|:----|
|and     |del      |from      |not      |while|
|as      | elif    |global    |or       |with |
|assert  | else    | if       |pass     |yield|
|break   | except  | import   |print
|class   | exec    | in       |raise
|continue| finally | is       |return 
|def     | for     | lambda   |try

are python keywords)

### Multiple Assignment

Python allows you to assign a single value to several variables simultaneously. For example:


    x = y = z = a = 1

Another way to use multiple assignment is to assign different values to different variables:


    x, y, z, a = 'Hello', 'World', 1, 2

> Test the output of above variables.

## Changing Storage Locations

Let's look at a very basic example of assignment operation:


    a = 10.0


    b = x


    x = 20

The first assignment is very basic, Python chooses a memory location for a and assigns 10.0 to it (Check a's data type!). The second assignment is more interesting:
Intuitively, one may assume that Python will find another location for the b and copy the value 10.0 to it (Like C or C++) but Python has its own way which is very efficient. Since a and b both will have the same values, Python decides to let b point to the memory location of a. Very efficient, right? Look at the third assignment operation. We are changing the value of b to 20.0. In this case, b gets its own memory location (Unlike C or C++ where the value would've changed). 
All this sounds good in theory, right? Let's prove it..


    a = 10.0


    a




    10.0




    b = a


    b




    10.0




    id(a)




    48719400




    id(b)




    48719400




    b = 20


    b




    20




    a




    10.0




    id(a)




    48719400




    id(b)




    42782640



> Check out the id function used here. It is again a built-in function that returns an integer which is guaranteed to be unique and constant for that 'object'. Consider it as a social security number for that 'object'. For C, C++ programmers, it is conceptually like memory addresses. You won't be using this function that often, but it's handy to know how variables/ objects are being moved around in your program (many debuggers actually use this function to keep tab on flow of your code).
