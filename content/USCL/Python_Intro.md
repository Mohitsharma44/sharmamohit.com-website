+++
Categories = ["Development", "Python", "USCL"]
Description = "Introduction to Python Programming Language"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-05-27T11:52:53-04:00"
title = "Python_Intro"

+++


<h1 align='center'>Introduction to Python</h1>

<img src="./python.png" alt="Python Logo" height="100" width="100" align='left'>    

----------------

## Python

`Python` is a great object-oriented, interpreted, and interactive programming language. It is widely used as general-purpose, high-level programming language. It is ranked among the [`top 5 programming languages`](spectrum.ieee.org/computing/software/top-10-programming-languages "Python is ranked 5th in the world") in the world. It can be used to create many things including web applications, desktop applications as scripting interpreter and many more.  There are no type declarations of variables, parameters, functions, or methods in source code. This makes the code short and flexible, and you lose the compile-time type checking of the source code. Python tracks the types of all values at runtime and flags code that does not make sense as it runs.


## Why IPython?

`IPython` is a command shell for **I**nteractive computing in **Python**. One of the feature of IPython that you will end up using frequently is the tab completion. It comes in handy especially when we import 3rd party packages like numpy and matplotlib which has hundreds of methods. IPython also has a set of pre-defined functions that you can call with a command line style syntax. One of the functions that you will find useful in debugging the errors in your code is %debug which will take you into python debugger and you can examine the source of your error. Also in your higher classes one of the function that you will be using is %timeit which basically measures the time that is required by your code to execute. You can check out more features of IPython on its webpage: [`IPython.org`](http://www.ipython.org 'Ipython Homepage')

##Let's get Started

The best way to learn python is to set it up and dive into it. Complete the [`installation`](newclasses.nyu.edu/access/content/group/9ce294e5-cc8b-44f8-963b-8160554a987f/Python%20Lab/Installation/Installing%20Python%20and%20Ipython "Installing Ipython and other dependencies for Python Lab") and come back to the following tutorial. Before we begin, I would like to point out that to learn the most from this lab, fire up your terminal and start typing the code you see in your ipython. 

> “Talk is cheap. Show me the code.” 
> `― Linus Torvalds`

## Python Syntax

The syntax of the Python programming language is the set of rules that defined how a Python program will be written and interpreted by the system (and by yourself). Python was designed to be a highly readable language. It has uncluttered visual layout and uses English keywords frequently. Python aims towards simplicity and generality in the design of its syntax. In fact Python's syntax guidelines are encapsulated in the mantra "There should be one and preferably only one obvious way to do it". You can read more about it in [`The Zen of Python`](www.python.org/dev/peps/pep-0020/ 'The Zen of Python').

### Indentation

Python provides no braces to indicate blocks of code for class and function definition (something we will come across later). Blocks of code are denoted by line indentation. The number of spaces or tabs in an indentation is variable but it is rigidly enforced. For example,


    if True:
        print 'True'
    else:
        print 'False'

    True


is indented by 4 spaces and will not generate any error. However an indentation like this


    if True:
        print 'True'
    else:
    print 'False'


      File "<ipython-input-2-bf47a0a38e2f>", line 4
        print 'False'
            ^
    IndentationError: expected an indented block



would generate an Indentation error as seen above

> Note: IPython automatically indents your code so you don't have to. However when you write your own code in a regular text editor like notepad, make sure to indent your code.
Note: Cross-platform compatibility note: because of the nature of text editors on non-UNIX platforms, it is unwise to use a mixture of spaces and tabs for the indentation in a single source file. It should also be noted that different platforms may explicitly limit the maximum indentation level.

Thus, if we want to add any more lines in the condition blocks, the lines should all have same level of indentation inside if block or else block.

### Multi-line Statements

Statements in Python typically ends with a new line. However python allows the use of the line continuation character ( \ ) to denote that the line should continue. For example:


    print "Hello \
    world"

    Hello world


will print Hello world in single line as show above. 

This is an explicit line joining technique
Another way to tell python not to end is by putting the strings or variables within the brackets ( ), { }, [ ] without using the line continuation character. For example:


    num = ['one', 'two', 'three'
           'four', 'five']


    num




    ['one', 'two', 'threefour', 'five']



This technique is known as implicit line joining technique 

> Note: The different brackets mean different things. We will study about them in later chapters. This is just to demonstrate a way of using multi-line statements.

### Quotations

You must have seen that in the above examples. we have used single and double quotes. Python accepts single, double and triple (''' or """)quotes to denote string literals. Bear in mind that the start quote and end quote should be of same type. Strings are generally created by using single or double quotes (python treats single and double quotes as the same.) Triple quotes are used when the string literals span across multiple lines. Consider following examples:


    name = 'USCL' 
    
    instructor = "Mohit"
    
    description = '''The UCSL at CUSP is a series of online sessions designed to build a 
    common skillset and familiarity with techniques, concepts, and models for 
    urban informatics computing. The online sessions focus on data explorations, 
    programming skills and statistical methods needed for scientific computing 
    in the field of Urban Informatics.'''

### Comments

#### Block

Block comments generally apply to some (or all) code that follows them, and are indented to the same level as that code. Each line of a block comment starts with a # and a single space. Paragraphs inside a block comment are separated by a line containing a single #. 


    # This is an 
    # example of a 
    # Block comment

#### Inline

An inline comment is a comment on the same line as a statement. Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space. Inline comments are unnecessary and in fact distracting if they state the obvious.


    x = 100  # Such inline comments are unnecessary

#### Docstrings

Docstrings are not necessary for non-public function, however you should use block comment that describes what the function does.  Docstrings are written between a triple quote (""" ...<docstring>...""").
