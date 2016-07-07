+++
Categories = ["Development", "Python", "USCL"]
Description = "Python Operators.. constructs that can manipulate the value of the operands"
Tags = ["Development", "Python", "USCL"]
author = "Mohit Sharma"
date = "2015-05-30T20:57:31-04:00"
title = "Python_Operators"

+++


<h1 align='center'>Python Operators</h1>

Operators in python are the constructs which can manipulate the value of operands. Simply put when operators are used with one or more than one operand, they produce some result. Consider a basic mathematical addition 1 + 2 in this case, 1 and 2 are operands and + is the operator. Operands can also be variables.
Python supports following types of operators:

- `Arithmetic Operators`
- `Relational (Comparison) Operators`
- `Assignment Operators`
- `Logical Operators`
- `Bitwise Operators`
- `Membership Operators`
- `Identity Operators`


## Arithmetic Operators

As the name suggests, Arithmetic Operators includes all the operators to perform basic arithmetic functions.

### Addition (+)

Addition operator adds the value of the operands on its either side. 


    2 + 2




    4



### Subtraction (-)

Subtracts right hand operand with the operand on the left hand.


    2 - 2




    0



### Multiplication ( * )

Multiplies the operands on its either sides and outputs the product.


    2 * 2




    4



### Division ( / )

Divides left hand operand with the right hand operand and outputs the quotient of the division.


    2 / 2




    1



### Modulus ( % )

Divides left hand operand with the right hand operate and outputs the remainder of the division.


    4 % 2




    0



### Exponential ( ** )

Performs exponential operation on the operands. The left hand operand is 'raised to' the right hand operand.


    4 ** 4




    256



### Floor Division ( // )

Divides the left hand operand with the right hand operand and outputs the quotient of the division removing the digits after decimal point.


    3.0 // 2




    1.0



## Relational Operators

Relational Operators compare the operands on either side and identifies the relation between them. These are also known as Comparison Operators. 

### Equal to ( == )

If the value of the two operands are equal, the condition becomes true.


    a, b = 10, 10


    a == b




    True



### Not Equal to ( != )

If the value of two operands are not equal, the condition becomes true.


    a != b




    False



### Greater than ( > )

If the value of the operand on the left hand side of the operator is greater than the value of the operand on the right hand side, the condition becomes true.


    a > b




    False



### Less than ( < )

If the value of the operand on the left hand side of the operator is less than the value of the operand on the right hand side, the condition becomes true.


    a < b




    False



### Less than OR Greater than ( <> )

If the value of the Operands on either side of the operator is not equal, the condition becomes true. It is equivalent to ' != '


    a <> b




    False



### Greater than OR Equal to ( >= )

If the value of the operand on the left hand side of the operator is greater than or equal to the operand on the right hand side, the condition becomes true.


    a >= b




    True



### Less than OR Equal to ( <= )

If the value of the operand on the left hand side of the operator is less than or equal to the operand on the right hand side, the condition becomes true.


    a <= b




    True



## Assignment Operators

Assignment operator is responsible for assigning some value to a variable. Example a = 2 .We have been doing this for quite sometime now, but assignment operator can be used in many other ways.



### Equals ( = )

Assigns the value from right hand side operand to the left hand side operand.


    a = 10

### Add AND ( += )

It is logically a two step process. In first step, the right hand side operand is added to the left hand side operand. In second step, the output of the first step is assigned to the operand on the left hand side.


    a += 10  # It is equivalent to a = a + 10

### Subtract AND ( -= )

It is also a two step process where the right operand is subtracted from the left operand and the result is assigned to the left operand. 


    a -= 10  # It is equivalent to a = a - 10

### Multiply AND ( *= )

The right operand is multiplied with the left operand and the result is assigned to the left operand.


    a *= 10  # It is equivalent to a = a * 10

### Divide AND ( /= )

The left operand is divided by the right operand and the quotient is assigned to the left operand.


    a /= 10  # It is equivalent to a = a / 10

### Modulus AND ( %= )

It takes the modulus of the two operands and assigns the result to the left operand


    a %= 10  # It is equivalent to a = a % 10

### Exponent AND ( **= )

It performs the exponential operation on the two operands and assigns the value to the left operand


    a **= 10  # It is equivalent to a = a ** 10

### Floor Division AND ( //= )

It performs floor division and assigns the quotient to the left operand.


    a //= 10 # It is equivalent to a = a // 10

## Bitwise Operator

Bitwise operator works on bits and performs operations bit by bit. Before we jump into the operator, lets revise the concept of Bits. At the smallest scale in computers, the information is stored in bits. Consider bit as a smallest unit of storage, just like an atom. A bit can only store binary values i.e 0's or 1's (but not both). n bits can store 2 to the power of n values (n 0's or 1's). Practically a bit is  very small for storage purposes, thus we deal with bytes which is equal to 8 bits. Then comes KiloBytes and MegaBytes and so on.. To understand the working of bitwise operators, we need to convert the operands to bits. 

To understand the conversion between decimal and binary numbers, watch this video:

[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/H4BstqvgBow/0.jpg)](https:/youtube.com/v/H4BstqvgBow)

For examples below, we will be using a, b = 6, 10. In python binary equivalent can be obtained by using a built-in function bin() which basically converts the integer to binary representation. If you followed the tutorial video above you must be writing full 8-bit representation for even a small integer. Python's bin() however only prints the bits that are necessary for representing the integer. For example,


    bin(6)   # To print the binary equivalent of integer 6




    '0b110'



> It did not print leading zeros (0b00000110)

> The leading 0b is for python to understand that the string representation means a binary number and not a regular string. Lets dive into the bitwise operators.

Let's get going with our examples. 


    a,b = 6, 10

### Binary AND ( & )

Operator uses two operands comparing them bit by bit. It outputs 1 if and only if both the operands have 1 at same bit location


    bin(a & b)




    '0b10'



 ### Binary OR ( | ) 
(The key above Return/ Enter key)

Operator uses two operands comparing them bit by bit. It outputs 1 if both the operands do not have 0 at same bit location.


    bin(a | b)




    '0b1110'



### Binary XOR ( ^ )

Operator uses two operands comparing them bit by bit. It outputs 1 if and only if both the operands do not have same bit value at same location.


    bin(a ^ b)




    '0b1100'



### Binary One's Complement ( ~ )

Operator uses single operand and toggles the bit value at every location.


    bin(~ a)




    '-0b111'



### Binary Left Shift ( << )

Operator shifts the bit location of the left operand towards left by the number of bits specified by the right operand.


    bin(a << 2)




    '0b11000'



### Binary Right Shift ( >> )

Operator shifts the bit location of the left operand towards right by the number of bits specified by the right operand.


    bin(a >> 2)




    '0b1'



## Logical Operators

Python supports three logical operators viz AND, OR and NOT.

### AND ( and )

If both the operands are true, the condition becomes true.

### OR ( or )

If any of the two operands are true, the condition becomes true.

### NOT (not)



Reverses the logical state of the operand.

## Membership Operator

This operator basically tests if the two operands are pointing at the same object or not. There are two types of membership operators:

Is

It evaluates to true if the operands on both the sides of the operator point to the same object.


    a =10


    b = a


    b is a




    True



### Is Not

It evaluates to true if both the operands do not point to the same object.


    a is not b




    False



## Identity Operator 

It is same as the python's Membership operator.

------------------
##Exercise:

- What will be the output of 3 / 2 ?
Is the output of 3.0/2 and 3 / 2 the same? Why or Why not?

- Is 'Six' == 'six' ?If not, why?

- Try assigning a to the power of 2, to the power of 2, to the power of 2 to a. (Check output of below code.)


    %%latex
    $$a = {{a^2}^2}^2 $$


$$a = {{a^2}^2}^2 $$


- Implement your own decimal to 8-bit binary converter. Convert decimal number 88 and see if the output is 01011000 .
- Consider an example below:


    a = 10
    b = a


    a == b




    True




    a is b




    True



What is the difference between ' == ' and ' is ' operator? Are they the same? What would happen if b is now assigned as 10 instead of a ?
