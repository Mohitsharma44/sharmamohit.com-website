+++
Categories = ["Development", "Python", "USCL"]
Description = "Introduction to Python Loops to keep the program doing some work again and again.."
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-01T01:57:59-04:00"
title = "Python_Loops"

+++


<h1 align='center'>Python Loops</h1>

Generally in python, statements are executed sequentially and once executed it is not repeated again. There may be a situation when you need to execute a piece of code n number of times, this is where the loops come in. Python has two types of loops viz. for loop and while loop. Lets take a look at an example:


    for i in range(3):
        print 'Hello World!'

    Hello World!
    Hello World!
    Hello World!



    while i > 0:
        print 'Hello World'
        i -= 1

    Hello World
    Hello World


As you can see, they both serve different purposes. For loop is used when you want to run something for fixed amount of times, whereas while loop can theoretically run forever (if you use something like `while True:`). 

## Working of Loops

If you've done any programming before, there's no doubt you've come across a for loop or an equivalent to it. In Python, they work a little differently. Basically, any object with an iterable method can be used in a for loop in Python. Even strings, despite not having an iterable method - but we'll not get on to that here. Having an iterable method basically means that the data can be presented in list form, where there's multiple values in an orderly fashion. You can define your own iterables by creating an object with next() and iter() methods (We will use this in later parts of the module). This means that you'll rarely be dealing with raw numbers when it comes to for loops in Python - great for just about anyone!

When you have a piece of code that you want to run x number of times, then code within that code which you want to run y number of times, you can use what is known as nested loops. In python these are heavily used with list (especially when it is a list of lists).
Example:


    # Nested Loops
    for i in xrange(5, 10):
        for y in xrange(11, 15):
            print 'i: %s\ty: %s'%(i, y)
            

    i: 5	y: 11
    i: 5	y: 12
    i: 5	y: 13
    i: 5	y: 14
    i: 6	y: 11
    i: 6	y: 12
    i: 6	y: 13
    i: 6	y: 14
    i: 7	y: 11
    i: 7	y: 12
    i: 7	y: 13
    i: 7	y: 14
    i: 8	y: 11
    i: 8	y: 12
    i: 8	y: 13
    i: 8	y: 14
    i: 9	y: 11
    i: 9	y: 12
    i: 9	y: 13
    i: 9	y: 14



    # List of Lists
    a = [[1,2,3], [4,5,6]]
    for lists in a:
        for x in lists:
            print x

    1
    2
    3
    4
    5
    6


## Loop Control Statements

Loop control statements change the executing of loop from its normal sequence. When execution leaves a scope, all automatic objects that were created in that scope are destroyed.

### Break Statement

It terminates the current loop and resumes the execution at the next statement. The most common use for break is when some external condition is triggered requiring a hasty exit from a loop. The break statement can be used in both while and for loops.
Example:


    for i in range(1, 10):
        if i == 5:
            print 'Condition satisfied'
            break
        print i  # What would happen if this is placed before if condition?

    1
    2
    3
    4
    Condition satisfied


From above example you can observe that when the value of i reached 5, the if condition was satisfied and the break statement was executed which stopped the for loop and exited.

### Continue

Continue statement returns the control to the beginning of the loop. The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
Example:


    x = 10
    while x > 0:
        x -= 1
        if x == 8:
            print 'Condition satisfied'
            continue
        print x
    
    #What is the difference when use the same code but in a for loop?

    9
    Condition satisfied
    7
    6
    5
    4
    3
    2
    1
    0


### Pass 

Pass is used when a statement is required syntactically but performs a null operation i.e. nothing happens when the statement is executed.
Example:




    for i in range(1, 10):
        if i == 5:
            print 'Condition satisfied'
            pass
        print i

    1
    2
    3
    4
    Condition satisfied
    5
    6
    7
    8
    9


As you can see execution of pass statement had no effect on the flow of the code. It wouldn't have mattered if it was not there. So when is it useful? It is generally used for temporary unimplemented logic. For example you have written a function and you are using if condition to test for something but before that you need to check the output of the code or just execute it. You can use pass statement. Python interpreter will read that and skip that part and get on with further execution.

## range and xrange

We used range and xrange in the examples of flow control statements. range function creates a list containing the numbers defined by the input. xrange on the other hand creates a number generator. The difference is very subtle but important based on what you are using it for. You will observe that xrange is used more frequently than the range function and the reason is resource usage. xrange generates (technically evaluates lazily) the numbers as needed whereas range creates the list of all the numbers at once. This means that using xrange less memory is used. Imagine a scenario where we are using loop control statements and somewhere in the code we need to exit the loop pre-maturely. If we use the range function, the memory is wasted creating the unused numbers. It might not sound like a big deal for small lists or small numbers but when you consider lists that hold data read from a csv file which has thousands of entries.. the difference is pretty significant.
