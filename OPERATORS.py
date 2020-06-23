# operators :  operators are special symbols in python in python that carryout the Arithematic or Logical computation \n
#              the value that the operator operates is called operand.
# types of oprators
#  Arithematic operaoter         (+,-,*,/,%,**)
#  Relational (or) Comparison    (<,>,<=,>=,==,!=)
#  Assisgnment                   (=,+=,-=,*=,/=,%=,//=,**=)
#  Bitwise                       (binary and,binary or,binary xor,binary ones component,binary leftshift,binary rightsift)
#  Logical                       (logical and &&,logical or ,logical not !)
#  Membership                    (in,not in)
#  identity                      (is,is not)
#  unary                         (-)

x = 10
y = 20
z = x+y
print(z)
z1 = x/2
print(z1)
x = 20
x+=10
print(x)
x = 30
x -= 50
print(x)
a,b = 10,20
print(a)
print(b)

c = a<b
print(c)
c1 = a>b
print(c1)
c2 = a<=b
print(c2)
c3 = a>=b
print(c3)
c4 = a==b
print(c4)
c5 = a!=b
print(c5)

h = 20
m = 30
d = h>25 and m<30
print(d)

h =  20
m =  30
d1 = h>25 or m<30
print(d1)

h =  20
m =  30
d2 = h>25 or m<30
print(d2)

x = True
print(x)
x = not True
print(x)

# Bitwise operators
# 1.compliment - (~)

x = ~15
print(x)
# print(bin(16))
# print(bin(15))
x = ~45
print(x)
# print(bin(46))
x = ~121
print(x)
# print(bin(121))
# print(bin(122))

# Bitwise-- AND(&)
x = 12&13
print(x)
x = 25&31
print(x)
# Bitwise---OR(|)
x = 12|13
print(x)
x = 25|31
print(x)
# Binary ---XOR (^)
x = 12^13
print(x)
x = 25^30
print(x)
# Binary left shift --- (<<)
x = 10<<2
print(x)
x = 9<<3
print(x)
x = 8<<4
print(x)
# Binary right shift ---(>>)
x = 10>>2
print(x)
x = 12>>4
print(x)
x = 13>>3
print(x)

# Importing math function .
# x = sqrt(25)  its wrong bcz we did  not import math function
# print(x)

import math
x = math.sqrt(25)
print(x)
x = math.sqrt(12)
print(x)
x = math.sqrt(15)
print(x)
x = math.floor(2.9)
print(x)
x = math.floor(2.1)
print(x)
x = math.floor(2.5)
print(x)
x = math.ceil(2.9)
print(x)
x = math.ceil(2.1)
print(x)
x = math.ceil(2.5)
print(x)

# print(help(math))

x = 3**2
print(x)
x = math.pow(3,2)
print(x)
x = 5**5
print(x)
x = math.pow(5,5)
print(x)
x = math.pi
print(x)
x = math.e
print(x)

# instead of writing ' math ' at all the we can write ' m ' aslo.
# here in this case both math,m work's.
# here  is a procedure,
import  math as m
print(math.sqrt(25))
print(m.sqrt(25))

from math import sqrt,pow
print(math.sqrt(35))
print(math.pow(8,8))

#x = 8
#y = 10
#z = x+y
#print(z)

# Getting input from the user
#x = input("enter 1st number is :")
#y = input("enter 2nd value :")
#z = x+y
#print(z)

#x =int(input("enter 1st number is :"))
#y =int(input("enter 2nd number is :"))
#z = x+y
#print(z)

# printing a character :
#char = input("enter a charecter is :")
#print(char)
#char = input("enter a charecter is :")
#print(char[0])
#char = input("enter a charecter is :")[0]
#print(char)

# calculating the expression
#char = input(" enter a charecter is :")
#print(char)

#result = eval(input("enter the expression:"))
#print(result)


