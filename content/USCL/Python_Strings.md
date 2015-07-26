+++
Categories = ["Development", "Python", "USCL"]
Description = "Strings and String manipulation in python"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-03T18:58:31-04:00"
title = "Python_Strings"

+++


<h1 align='center'>Python Strings</h1>

A python string is usually a bit of text that you want to display or use or export out of the program that you are writing (to a file or over the network). Python has a built-in string class named str with many handy features. Python knows you want something to be a string when you enclose the text with either single quotes ( ' ) or double quotes ( " ). You must've seen this in our previous tutorials. If not, check a very basic example below:


    a = 'Hello World'
    print a
    type(a)

    Hello World





    str



A string literal can span multiple lines, to do that there must be a backslash ( \ ) at the end of each line to escape the newline because by default the return key on the keyboard is considered as end of line. However if you do not feel comfortable using backslashes, you can put your text between triple quotes ( """ ) or ( ''' ). If you don't want characters prefaced by \ to be interpreted as special characters, you can use raw strings by adding an r before the first quote. A very basic example would be something like this:


    print 'C:\name\of\dir'  # Using triple quotes also will not help you

    C:
    ame\of\dir



    print r'C:\name\of\dir'

    C:\name\of\dir


## String Concatenation

Just like Python numerical types, Python strings are 'immutable'. What it means is that they cannot be changed after they are created. So if we concatenate the two strings, python will take the two strings and build a third string with the concatenated value or the first and second string. 


    a = 'Hello'  # String 1
    b = 'World'  # String 2
    c = a + b  # Concatenate two string as String 3


    c




    'HelloWorld'



> Prove the above.. Hint: Refer Python Variables

Concatenation of strings will also happen when the string literals are placed next to each other.


    'Hello' 'World'




    'HelloWorld'



Concatenation can also be preformed on variables of same datatype. i.e a string concatenation can only be performed on two strings or two variables that have str as their datatype. If you try to perform string concatenation on a string and an integer, Python will trow a typeError. String Concatenation also comes in handy when we have to break long strings (without using backslashes):


    a = 'Hello'
    b = 1
    a+b


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-7-fbd202b10ae9> in <module>()
          1 a = 'Hello'
          2 b = 1
    ----> 3 a+b
    

    TypeError: cannot concatenate 'str' and 'int' objects



    a = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac urna volutpat, interdum nibh in'
         'aucibus odio. Integer tempus, est ut faucibus efficitur, nibh est elementum ex, at vulputate urna purus at arcu.')


    a




    'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque ac urna volutpat, interdum nibh inaucibus odio. Integer tempus, est ut faucibus efficitur, nibh est elementum ex, at vulputate urna purus at arcu.'



## String Indexing

Characters in a string can be accessed using the standard [ ] syntax. Python uses zero-based indexing which means that first character in a string will be indexed at 0 location. So for example if the string is 'Python' then, it can be shown to be indexed as:


    a = 'Python'


    len(a) # Total number of items/ characters in a string




    6




    a[0]




    'P'




    a[-6]




    'P'




    a[0] = 'J' # It will result in an error because Strings are immutable.


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-421b14552e81> in <module>()
    ----> 1 a[0] = 'J' # It will result in an error because Strings are immutable.
    

    TypeError: 'str' object does not support item assignment


Notice the `In [4]`: We printed the negative index number!! How?


     +---+---+---+---+---+---+
     | P | y | t | h | o | n |
     +---+---+---+---+---+---+
        0   1  2   3   4    5 
       -6  -5 -4  -3  -2   -1

When you enter a non negative index value, it is considered as indexed from left to right and when you enter the negative index values (negative indexing starts from -1), python's interpreter is intelligent enough to understand that you meant to get the value indexed from right to left.

## String Slicing

The 'Slice' syntax is a handy way to refer to sub-parts of strings. The slice a[start : end] is the elements beginning at start and extending up to end (not including end). Look at the above Python string literals representation and work on following examples:


    a = 'Python'


    a[0:2]




    'Py'




    a[:-4]  # Remember in a[start:end], end is not included




    'Py'




    a[:-4] + a[2:]  # This even works for negative or out of bounds




    'Python'



## % Operator

Everything that we have seen till now had a string that cannot be modified but what if we now want to modify few words of the string and leave the remaining string unmodified?
For people familiar with C++, Python has a printf() - like facility to put together a string using % operator. Python uses %d operator to insert an integer specified in a tuple, %s and for string and %f for floating point(we shall discuss about tuple next week. For now just consider tuple as a group of values inside parenthesis separated by commas.) Example:


    text = '%s World. %s %d %d %f'


    text %('Hello', 'Check', 1, 2, 3)




    'Hello World. Check 1 2 3.000000'




    text %('Hola', 'Testing', 1, 2, 5.6789)




    'Hola World. Testing 1 2 5.678900'



## Unicode Strings

Starting with Python 2.0 a new data type for storing text data is available to the programmer: the Unicode object. It can be used to store and manipulate Unicode data (see http://www.unicode.org/) and integrates well with the existing string objects, providing auto-conversions where necessary.
Unicode has the advantage of providing one ordinal for every character in every script used in modern and ancient texts. Previously, there were only 256 possible ordinals for script characters. Texts were typically bound to a code page which mapped the ordinals to script characters. This lead to very much confusion especially with respect to internationalization (usually written as i18n — 'i' + 18 characters + 'n') of software. Unicode solves these problems by defining one code page for all scripts.


Creating Unicode strings in Python is just as simple as creating normal strings:


    a = u'Hello World'


    a




    u'Hello World'




    type(a)  # What would have been the output if a = 'Hello World'?




    unicode



The small 'u' in front of the quote indicates that a Unicode string is supposed to be created. If you want to include special characters in the string, you can do so by using the Python Unicode-Escape encoding. The following example shows how:


    a = u'Hello\u0020World' 


    a




    u'Hello World'



The escape sequence \u0020 indicates to insert the Unicode character with the ordinal value 0x0020 (the space character) at the given position. (If you want to print the unicode as plain text you need to escape the backslash with another backslash and in the output you will see 4 backslashes. To get rid of so many backslashes, ts better to use raw mode as discussed in the beginning.)

The built-in function unicode() provides access to all registered Unicode codecs (COders and DECoders). Some of the more well known encodings which these codecs can convert are Latin-1, ASCII, UTF-8, and UTF-16. The latter two are variable-length encodings that store each Unicode character in one or more bytes. The default encoding is normally set to ASCII, which passes through characters in the range 0 to 127 and rejects any other characters with an error. When a Unicode string is printed, written to a file, or converted with str(), conversion takes place using this default encoding.


    u'äöü'




    u'\xe4\xf6\xfc'




    str(u"äöü")  # This will raise UnicodeEncodeError. Think, Why?


    ---------------------------------------------------------------------------

    UnicodeEncodeError                        Traceback (most recent call last)

    <ipython-input-28-f7a5ab2207b1> in <module>()
    ----> 1 str(u"äöü")  # This will raise UnicodeEncodeError. Think, Why?
    

    UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)


To convert a Unicode string into an 8-bit string using a specific encoding, Unicode objects provide an encode() method that takes one argument, the name of the encoding. Lowercase names for encodings are preferred.

## Built-in String Methods

Now that we know about the string and some basic manipulation on strings, lets look at some more built-in methods that can be used. 

### capitalize

It returns a copy (remember the same string is not modified because strings are immutable) of the string with only its first character capitalized.
Example:


    a = 'python'
    a.capitalize()




    'Python'



### center

Return YOUR STRING centered in a string of length width. Padding is done using the specified fill character (default is a space).
Example:


    a.center(10, '!')




    '!!python!!'



### count

The method count() returns the number of occurrences of a sub-string in the range [start, end].
Example:


    a.count('o', 0, len(a))




    1



### decode

This method decodes the string using codec registered for encoding. 
Example:


    a = '\xc3\xa4\xc3\xb6\xc3\xbc'


    b = a.decode(encoding = 'utf-8')


    b




    u'\xe4\xf6\xfc'




    print u'%s' %b

    äöü


### encode

Returns encoded version of a string.
Example:


    a = u'äöü'


    a




    u'\xe4\xf6\xfc'




    a.encode('utf-8')




    '\xc3\xa4\xc3\xb6\xc3\xbc'



### endswith

TRUE if the string ends with the specified suffix, otherwise FALSE.


    a = 'Hello World'


    a.endswith('World')




    True



### expandtabs

It returns a copy of the string in which tab characters i.e. '\t' are expanded using spaces, optionally using the given tabsize.


    a = 'Hello \t World'


    a




    'Hello \t World'




    a.expandtabs(16)




    'Hello            World'



### find

It determines if the sub string occurs in string. Optionally between beg and end. If found, it returns the index value. Otherwise returns -1
Example:


    a = 'This is a test string'


    b = 'str'


    a.find(b)




    15



### rfind

Same as find() but searches backwards in string

### index

Same as find but raises an exception if sub string is not found.

### isalnum

Returns true if the string has at least one character and all characters are alphanumeric and false otherwise.
Example:


    a = 'Welcome2015'


    a.isalnum()




    True



### join

Concatenates the string representations of elements in sequence into a string, with separator string.
Example:


    a = ''


    b = ('p', 'y', 't', 'h', 'o', 'n')
    a.join(b)




    'python'



### strip

Returns a copy of string in which all chars have been stripped from the beginning and the end of the string.
Example:


    a = '....This is Python....'
    a.strip('.')




    'This is Python'



### lstrip

Removes all leading whitespaces in a string.
Example:


    a = '.......python'
    a.lstrip('.')




    'python'



### rstrip

Removes all trailing whitespaces in a string.

### max

Returns the maximum alphabetical character from the string.
Example:


    a = 'python'
    max(a)  # This is very helpful when used with integers




    'y'



### min

Returns the minimum alphabetical character from the string.

### replace

Returns a copy of the string with all occurrences of sub string old by new. If the optional argument max is given, only the first count occurrences are replaced.
Example:


    a = 'This is Python'
    a.replace('is', 'was', 1)




    'Thwas is Python'



### rjust

Returns a space-padded string with the original string right-justified to a total width of width column
Example:


    a = 'Python'
    a.rjust(10,'$')




    '$$$$Python'



### split

Returns a list of all the words in the string separated by a separator string.
Example:


    a = 'This is Python'
    a.split(' ')




    ['This', 'is', 'Python']



These are the methods that you will end up using mostly. However, there are many more built in methods that you can access by pressing tab after typing the variable name whose type is str. 
