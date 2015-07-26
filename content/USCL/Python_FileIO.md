+++
Categories = ["Development", "Python", "USCL"]
Description = "File handling in Python"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-06-26T02:07:12-04:00"
title = "Python_FileIO"

+++


<h1 align='center'>Python File I/O</h1>

Before we jump in to file I/O functions, lets first look at some basic I/O functions that are available to use in Python. 
In Python, there are three basic I/O connections, Standard Input, Standard Output and Standard Error. As the name suggests, Standard Input is the data that goes to the program through the keyboard. keyboard being the standard input. Standard output is the terminal console, unless redirected..(guess where?!!) and Standard error is the stream where the programs write their error messages which is again to the terminal unless redirected.

## Standard Input:

Python provides two built-in functions to read a line from the keyboard.

### raw_input

The raw_input( ) function reads one line from the standard input and returns it as a string. 
Example:


    # Create a file test_input.py and write this:
    str = raw_input('Enter your name')
    print 'Hello',str
    # Now run the file as python test_input.py and input your name.

    Enter your nameMohit
    Hello Mohit


Pretty easy right? When you execute the file, it will prompt you to enter your name and print 'Hello <name>'.

### input

The input function is equivalent to raw_input, except that it assumes the input is a valid Python expression, evaluates and returns the result.
Take the previous file and replace raw_input by input and execute the code. Now enter this when prompted for input:


    str = input('Enter your name')
    print 'Hello',str

    Enter your name[x for x in range(10)]
    Hello [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


## File I/O

Until now you have been reading and writing to the standard input. Lets now perform the same function to the files. Now we will see how we can read and write to the files.

##Opening Files: 

Files can be opened using python's built-in open() function. This function creates a file object which we will use for performing operations on the file. It will become much clear when we look at a complete example. For now, just remember that we need to create a file object before performing any file I/O and try to remember the syntax.
Syntax:

`f = open(file_name, access mode, encoding)`

file_name: The file name that you would like to perform your I/O operations on.
encoding: Encoding tells python what encoding scheme to use to convert the stream of bytes to text. 
access_mode: This is the mode which determines if the file is to opened as read only,read-write, write only etc modes. The ways in which a file can be opened is mentioned below:


|String | Its Function|
|:------|------------:|
|r	|Opens a file as read only|
|rb	|Opens a file as read only in binary format|
|r+	|Opens a file for reading and writing|
|rb+	|Opens a file for reading and writing in binary format|
|w	|Opens a file for writing only|
|wb	|Opens a file for writing only in binary format|
|w+	|Opens a file for both reading and writing|
|wb+	|Opens a file for writing and reading in binary format|
|a	|Opens a file for appending|
|ab	|Opens a file for appending in binary|
|a+	|Opens a file for appending and reading|
|ab+	|Opens a file for appending and reading in binary format|

## Reading and Writing

Once we have created a file object we can perform many operations on the file object which, like all objects, has methods to take care of nitty gritty details and perform the operations on the file. We will now look at some of the attributes of the file object.

### file_object.close()

This method will close the file that we have currently open. You should always call this method once you are done performing I/O operations on the file using the file object.

### file_object.softspace

It returns a boolean indicating whether a space character needs to be printed before another value using the print statement. It is kind of a read-write attribute that is used internally by the print statement to keep track of its own state and not by the file object.

### file_object.flush()

This method requests that the file object's buffer to be written out to the operating system, ensuring that the file (as seen by the system) has exactly the contents that the file_object has. (By default python uses operating systems buffer so you don't have to call this, unless you configure it otherwise. It is mainly used for tty devices.)

### file_object.isatty()

This method returns true if the file_object is an interactive terminal (tty is a special device that lets people who are deaf, hard of hearing or speech-impaired to communicate)

### file_object.mode

This is a read-only attribute that is the value of the mode string used in the open call that created the file_object

### file_object.name

This is also a read-only attribute that is the value of the filename string used in the open call that created the file_object.

### file_object.readline([size])

This method reads strings from the file till it reaches new line character ( '\n' ) if the 'size' parameter is empty. If an integer is provided as size parameter, then this method returns string of length size.

### file_object.readlines([size])

This method basically calls the readline() method till it reaches the end of file.

### file_object.seek(pos, how=0)

Sets the file_object's current position to the signed integer byte offset by pos from the reference point. The how parameter, which is 0 by default, indicates the reference point. how=1 is the reference of current position and how=2 is the reference of the end of the file.

### file_object.tell()

This method tells the current file position when you are reading from or writing to a file.

### file_object.truncate([size])

This method truncates the file to be at most of size size.  If you don't mention the size it takes the size from f.tell() method as the new size.

### file_object.write(str)

Writes the bytes of string str to the file.

### file_object.writelines(lst)

Writes sequence of strings to file. No new line is added automatically.

Examples:

Let's create a file and perform some interesting I/O operations on it.


    # Create a .py file or follow along in Ipython terminal
    try:
        f = open('test.txt', 'w')  # If there is a test.txt file in your current location, this step will overwrite it. So change file_name if you want
        print 'Cursor position in the file before writing: ',f.tell()
        f.write('Hello World')
        print 'Cursor position after writing: ',f.tell()
    except IOError, e:
        print 'Error performing I/O operations on the file: ',e
    finally:
        if f:  # If file_object exists,
            f.close()

    Cursor position in the file before writing:  0
    Cursor position after writing:  11


Yaay! You created your first file and wrote 'Hello world' to it! Lets edit it now!


    try:
        f = open('test.txt', 'r+')
        print f.readline()
        f.writelines(['\n', 'This is', 'Python'])
        f.seek(0)  # Go to the starting of file
        print f.readlines()  # Read all the lines in the file.
        f.truncate(20)
        f.seek(0)
        print 'After truncate: ',f.readlines()
    except IOError, e:
        print 'Error performing I/O on file ',e
    finally:
        if f:
            f.close()

    Hello World
    ['Hello World\n', 'This isPython']
    After truncate:  ['Hello World\n', 'This isP']


Great! So now we opened the file, read its contents, added multiple strings, truncated and closed it! This covers pretty much everything that you will need when you are working with almost any kind of file that has some text.

------
## Exercise: 

Create a binary file and write 'Hello World' in it. Now create an ascii file and add the same text to it. Read both the files. Is there any difference between the two? 



## CSV (Comma Separated Values)

In the above examples, we saw how to perform read-write operations on a file. This is generally used for files that have multiple lines of strings. However if you have data like this:

||||
|:--|:--|:--|
|Data1	|Data2	|Data3|
|Example1	|Example2	|Example3|

It is stored in a file with this format:

Data1, Data2, Data3

Example1, Example2, Example3

As can be seen in the above example, each row is a new line, and each column is separated with a comma. Many online services such as an online bank allow its users to export tabular data from the website into a CSV file. These files can then be opened and viewed offline using a Spreadsheet program such as Microsoft Excel.

### So why do we need such CSV files? 
There are two primary reasons for the existence of this format:

- CSV are plain-text files which makes them easy to store and read from
- CSV files are stored as sequence of human readable characters, thus making it easy for humans to interpret the data without requiring any format conversion.

CSV is a delimited text file that uses a comma to separate values (many implementations of CSV import/export tools allow other separators to be used). Simple CSV implementations may prohibit field values that contain a comma or other special characters such as newlines. More sophisticated CSV implementations permit them, often by requiring " (double quote) characters around values that contain reserved characters (such as commas, double quotes, or less commonly, newlines). Embedded double quote characters may then be represented by a pair of consecutive double quotes, or by prefixing an escape character such as a backslash (for example in Sybase Central). The name "CSV" indicates the use of the comma to separate data fields. Nevertheless, the term "CSV" is widely used to refer a large family of formats, which differ in many ways. Some implementations allow or require single or double quotation marks around some or all fields; and some reserve the very first record as a header containing a list of field names. An official standard for the CSV file format does not exist.

Download a Sample\* CSV file from [`HERE`](https://newclasses.nyu.edu/access/content/group/9ce294e5-cc8b-44f8-963b-8160554a987f/Python%20Lab/Week3/Python%20File%20I_O/sample.csv 'Sample CSV') and save it in your current folder location. 

>Disclaimer: The data generated is completely random using a third party website [`https://www.fakenamegenerator.com`](https://www.fakenamegenerator.com 'FakeName Generator')



### Reading CSV files

reader() can be used to create an object that is used to read the data from a csv file. The reader can be used as an iterator to process the rows of the file in order. Lets take a look at an example:
Example


    # You can create a new file or follow along in Ipython terminal
    row = []
    import csv  # Importing csv module
    try:
        f = open('sample.csv', 'r')
        reader = csv.reader(f)
        for i in reader:
            row.append(i)
    except IOError, e:
        print 'Error: ',e
    finally:
        if f:
            f.close()
            
    row[0:10]




    [['\xef\xbb\xbfGivenName', 'Gender', 'Title', 'Occupation', 'City'],
     ['Nicholas', 'male', 'Mr.', 'Speech writer', 'Plantation'],
     ['Jeanette', 'female', 'Mrs.', 'Surfacing equipment operator', 'Chicago'],
     ['David', 'male', 'Mr.', 'Engineering geologist', 'Worthington'],
     ['Susan',
      'female',
      'Ms.',
      'Cutting, punching, and press machine tender',
      'Fulton'],
     ['Dennis', 'male', 'Mr.', 'Construction millwright', 'Fargo'],
     ['Susan', 'female', 'Mrs.', 'Private investigator', 'Blackwood'],
     ['John', 'male', 'Mr.', 'Chemical engineering technician', 'Marietta'],
     ['Damon', 'male', 'Mr.', 'Loan closer', 'Mansfield'],
     ['George', 'male', 'Mr.', 'Public defender', 'Minneapolis']]



reader() is a method available in csv package so the first line is importing the csv package. The reader() method takes sequence or an iterable file object, and returns an iterator. As the csv file is being read, each row of the input data is converted to a list of strings. The parser handles the line breaks embedded within the strings which is why using row is not always the output that you might get when taking a line input from file. 

### Writing CSV files

Writing csv files is just as easy as reading them. To write to a csv file, we can use writer() method to create an object for writing and then iterate over the rows using csv's writerow() method to write it.
Example:


    import csv
    try:
        f = open('test.csv', 'w')
        writer = csv.writer(f)
        for i in range(10):
            writer.writerow((i, i+1, i+2))
    except IOError,e:
        print 'Error: ',e
    finally:
        if f:
            f.close()


Now try opening the file just like we did before. 

### Using Field Names

In addition to working with sequences or data, the csv module includes classes for working with rows as dictionaries so that the fields can be named. The DictReader and DictWriter classes translate rows to dictionaries instead of lists. Keys for the dictionary can be passed in, or inferred from the first row in the input.




    try:
        f = open('sample.csv', 'r')
        reader = csv.DictReader(f)
        for i in reader:
            row.append(i)
    except IOError, e:
        print 'Error: ',e
    finally:
        if f:
            f.close()
    
    row[0:10]




    [['\xef\xbb\xbfGivenName', 'Gender', 'Title', 'Occupation', 'City'],
     ['Nicholas', 'male', 'Mr.', 'Speech writer', 'Plantation'],
     ['Jeanette', 'female', 'Mrs.', 'Surfacing equipment operator', 'Chicago'],
     ['David', 'male', 'Mr.', 'Engineering geologist', 'Worthington'],
     ['Susan',
      'female',
      'Ms.',
      'Cutting, punching, and press machine tender',
      'Fulton'],
     ['Dennis', 'male', 'Mr.', 'Construction millwright', 'Fargo'],
     ['Susan', 'female', 'Mrs.', 'Private investigator', 'Blackwood'],
     ['John', 'male', 'Mr.', 'Chemical engineering technician', 'Marietta'],
     ['Damon', 'male', 'Mr.', 'Loan closer', 'Mansfield'],
     ['George', 'male', 'Mr.', 'Public defender', 'Minneapolis']]



Run this and see the difference in the output. 

Similar to DictReader, we also have DictWriter which needs to be given a list of field names so it know how to order the columns in the output file. 
Example:


    import csv
    try:
        fieldnm = ('Title1', 'Title2', 'Title3')
        f = open('test.csv', 'w')
        writer = csv.DictWriter(f, fieldnames=fieldnm)
        headers = dict((i, i) for i in fieldnm)
        for i in range(10):
            writer.writerow({'Title1':i, 'Title2':i+1, 'Title3':i+2})
    except IOError,e:
        print 'Error: ',e
    finally:
        if f:
            f.close()


This technique is good when the filesize (or the number of columns) is not very big. When the row numbers starts scaling up, the list that is created by the reader() method starts growing in memory and makes the process very very slow. 
We will generally be dealing with the files that have over a million row entries and this method is not the most efficient way of dealing with such files. To handle such 'Big Data', we will study a python package called Numpy in the next week.
