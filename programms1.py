# python program which accepts the radius of  a circle from user and compute area

#from math import pi
#r = float(input ("Input the radius of the circle :  "))
#print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))    # str() function returns a string containing a nicely printable representation of an object.

#frommath import pi
#r = float(input("enter the radius of circle : "))
#area = pi*r*r
#print("Area of a circle is : ",area)

n = (10,20,30,40,50)
print(n[1])

pi = 3.14
r  =  15
print("Area of circle is :",pi*r*r)

from math import pi
r = 20
print("Area of the circle is :", pi*r*r)


fname  = 'ravi'
lname  = 'kakarla'
fnname = str(lname)+" " + str(fname)
print("Hello :",  fnname)


# Write a Python program which accepts a sequence of comma-separated numbers from  \n\t
# user and generate a list and a tuple with those numbers.

x = (1,2,3,"ravi","kakarla","chowdary",10.5,1.2,9.6,7.4,4,5,6,7,8,9,9)
print(list(x))
print(tuple(x))

#The split() method splits the string into substrings \n\t
#if it finds instances of the separator:

#values = ("input some comma separated numbers : ")
#List   = values.split(" , ")
#Tuple  = tuple(List)
#print(List)
#print(Tuple)

n = "ravindra , chowdary , kakarla"
print(n.split(","))

# wrong
#values  = ("input some comma seperated numbers :")
#print(values)
#List  = (+str(list(values)))
#print(List)
#Tuple = (+str(tuple(values)))
#print(Tuple)


myfilename = 'california girls.mp3'
print(myfilename.partition("."))

# Write a Python program to accept a filename from \n\t
# the user and print the extension of that.

# The split() method splits the string into substrings \n\t
# if it finds instances of the separator:

#fn= input("Enter Filename: ")
#f = fn.split(".")
#print ("Extension of the file is : " + f[-1])

# repr() returns a string that holds a printable representation of an object.

#filename = input("write the filename : ")
#file_extns = filename.split(".")
#print("the extension is" +repr(file_extns[-1]))

# write a pyhton program to accept a filename from the user \n\t
# to print the extension of the file
#filename = input("enter the name of the of file  ")
#f = filename.split(".")
#print(" the extension of the file is " +repr(f[-1]))

# Write a Python program to display the first and last colors from the following list.
#colour_list= ["Red","Green","White" ,"Black"]
#print(colour_list[0],",",colour_list[-1])

#colour_list= ["Red","Green","White" ,"Black"]
#print("the first colour is " + colour_list[0]+ "and the last colour is "+ colour_list[1])
#print(colour_list[::-1])
#print([colour_list[0]])

colour_list= ["Red","Green","White","Black"]
print(colour_list[::])
print(colour_list[::-1])
# wrong justification  print(colour_list["colour_list"-1])

# Write a Python program to display the examination schedule.
# (extract the date from exam_st_date).
#  exam_st_date = (11, 12, 2014)
# Sample Output: The examination will start from : 11 / 12 / 2014
exam_st_date = (11,12,2014)
#print("The examination will start form : %i / %i / %i"%(11,12,2014))
#print("The examination will start from : %i / %i / %i "%exam_st_date)
print(f"the examination will start from : {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[1]}")

exam_st_date = (11, 12, 2014)
day, month, year = exam_st_date
print("The examination will start from : {}/{}/{}".format(day,month,year))

s = "ravi","kakarla","chowdray"
s = " "
print(s)

list = [1,2,3,4,5,6,7,8,9]
list.clear()
print(list)

tuple = (1,2,3,4,5,6,7,8,9)
tuple = ""
print(tuple)

#filename = input("enter the name of the file with extension : ")
#file_extn = filename.split(".")
#print("the extension of the file is :"+repr(file_extn[-1]))

#exam_st_date = 10,8,2012
#print(f" the examination date is :  ,{ exam_st_date {0}/ exam_st_date {1} / exam_st_date {2}}")
#     (or)
exam_st_date = (10,2,2020)
#E = exam_st_date.split(".")
print("the examination date is : %i/%i/%i " %exam_st_date)
#print(f"The examination will start from : {exam_st_date[0]}/{exam_st_date[1]}/{exam_st_date[2]}")
#print( "The examination will start from : %i / %i / %i"%exam_st_date)

# Write a Python program that accepts an integer (n) \n
# and computes the value of n+nn+nnn.

# correct

#a   =  int(input("enter an integer value : "))
#n1  =  int("%s" %a)
#n2  =  int("%s%s" %(a,a))
#n3  =  int("%s%s%s" %(a,a,a))
#print(n1+n2+n3)

#wrong

#n   =  int(input("enter an integer value : "))
#answer = int(n) + int(n*n) + int(n*n*n)
#print(f"the Answer is : " , (answer))

#wrong

#n=int(input("Enter the value : "))
#answer= int(n) + int(n*n) + int(n*n*n)
#print(f"Answer is :" , (answer))

# correct

#n=input("Sample value of n is:")
#sum=int(n)+int(n+n)+int(n+n+n)
#print("Expected result:",sum)

# wrong

#n=int((input('enter a value of n :')))
#n1=n*10+n
#n2=n*100+n1
#print(n1+n2+n)

# correct

#import math
#num1 = input("enter a number")
#num2 = int(num1) + int(num1*2) + int(num1*3)
#print(num2)

#n = input(" The symbol is : ")
#print(" %s "%n)
#print(" %s %s " %(n,n))
#print(" %s %s %s " %(n,n,n))

# wrong

#a=int(input("input the value"))
#b=a+11*a+111*a
#print(b)

# Write a Python program to print the documents (syntax, description etc.) of \n\t
# Python built-in function(s).


print(abs.__doc__)
#print(my__str.__doc__)

import builtins

#fun = input("Enter the function of which you want to check description:")
#my_str = getattr(builtins, fun)
#print(my_str.__doc__)

# Write a Python program to print the calendar of a given month and year.
#import calendar
#x = int(input("enter the year of the calendar :"))
#y = int(input("enter the month of the calendar :"))
#print(calendar.month(x, y))

#import calendar
#the_date = input("Please enter a month and a year separated by a comma: ")
#date_list = the_date.split(",")
#my_month = int(date_list[0])
#my_year = int(date_list[1])
#print(calendar.month(my_year , my_month ))

#import calendar
#print(calendar.month(theyear=2019,themonth=6))

# Write a Python program to print the following 'here document'.
x = ('''
       a string that you "don't" have to escape
       this
       is a......multi-line
       heredoc  string --------> example
       ''')
print(x)

x = (''' a string that you "don't" have to escape \n this \n is a......multi-line \n heredoc  string --------> example \n ''')
print(x)

# Calculate number of days between two dates.
import datetime
x = datetime.date(year=2019,month=6,day=12)
y = datetime.date(year=2019,month=6,day=18)
print(y.day-x.day)

from datetime import date
st__date = date(2018,11,6)
nd__date = date(2019,12,18)
day =nd__date-st__date
print(day.days)

# Write a Python program to get the the volume of a sphere with radius 6.
#r = int(input("enter the radius of sphere : "))
#y = (4/3)*(pi)*(r**3)
#print(" the volume of the sphere is :", y)


#pi = 3.1415926535897931
#r  = 6.0
#V  = 4.0/3.0*pi* r**3
#print('The volume of the sphere is: ',V)

#import math

#r = int(input("Input the radius : "))

#v = float(((4/3)*math.pi)*math.pow(r,3))

#print("The result is : ",math.ceil(v))


# List programms :-

# Write a Python program to sum all the items in a list :-
list = [1,2,3,4]
x  = sum(list)
print(x)

#y =int(input(" enter the values "))
#z = list(y)
#x  = sum(z)
#print(x)

#x = [1,2,3]
#y = tup(x)
#print(y)

#x = 'ravi','kakarla','chowdary'
x = [1,2,3,4,5,6,7,8,9]
print(x[1:5])
x = (1,2,3,4,5,6,7,8,9)
print(x[1:5])

#x = [1,2,3]
#y = tuple(x)
#print(y)

#Convert list to tuple
#x = [5, 10, 7, 4, 15, 3]
#print(x)
#use the tuple() function built-in Python, passing as parameter the list
#tuplex = tuple(x)
#print(tuplex)

# Initialisation of list
#Input = ['Geeks', 'for', 'geeks']

# Using list Comprehension
#Output = tuple([name] for name in Input)

# printing output
#print(Output)

# Write a Python program to multiplies all the items in a  list.
#x = [1,2,3,4,5]
#y = x[0]*x[1]*x[2]*x[3]*x[4]
#print(y)

x = [1,2,3,4,5,6,7,8]
mul = 1
for i in x:
    z = 1
    y =z*i
    mul = mul*y
print(mul)

# Write a Python program to get the largest number from a list.
x = [55,105,28,32,50]
y = max(x)
y1 = min(x)
print(y)
print(y1)

list1, mul = [1, 2, -8] , 1
for i in list1:
    mul *= i
print(mul)

mul = 1
m=[2,5,-5,7]
for i in m:
    mul=i*mul
print(mul)


x = [1,2,3,4,5,6,7,8]
mul = 1
for i in x:
    mul = i*mul
print(mul)


list1 = [1,2,3,4]
length = len(list1)
result = 1
for i in range(1,length+1):
    result = result*i
print(result)

def max__num__in__list(list):
    max = list[0]
    for a in list:
        if a>max:
            max = a
    return max
print(max__num__in__list([1,2,-8,0]))


def min__number__in__list(list):
    min = list[0]
    for i in list:
        if i<min:
            min = i
        return min
print(min__number__in__list([1,50,33,56,98]))


# Write a Python program to count the number of strings ,\n
# where the string length is 2 or more and \n
# the first and last character are same from a given list of strings.

def  match__words(words):
    ctr = 0

    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            print(word,end=",")
            ctr = ctr+1
    return ctr

print(match__words(["abc","kak","kik",'102','105','101','252']))



#mygenerator = (x*x for x in range(3))
#for i in mygenerator:
    #print(i)


# Write a Python program to get a list, sorted in increasing order by \n
# the last element in each tuple from a given list of non-empty tuples.

x  = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
x.sort()
print("sorted list : ", x)

# o/p reqires [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

# Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]  # O/P = [10,20,30,40,50,60,80]

dup_items    =  set()
uniq_items =  []
for x in a :
    if x not in dup_items:
        uniq_items.append(x)
        dup_items.add(x)

print(dup_items)

#a = [10,20,30,20,10,50,60,40,80,50,40]
#print(list(set(a)))
x=[1,2,3,4,5,4,3,2]
duplicate=set(x)
print(duplicate)

x = {1,1,2,2,3,4,5,6,6,5,4,3,2,1,2}
print(x)


a = [10,20,30,20,10,50,60,40,80,50,40]
A = set(a)
print(A)

#b = (11,11,22,22,33,44,55,66,66,55,44,33,22,11,22)
#c = set(b)
#print(list[c])

# 'not in' operator- Evaluates to true if it does not finds a variable \n
# in the specified sequence and false otherwise.
#  Write a Python program to check a list is empty or not.
a = [ ]
if not a:
    print("list is empty")
else:
    print('list is having values')

# a = [2,3]
# if not a:
#    print("list is empty")
#else:
#    print('list is having values')
a = [ ]
y = len(a)
if y==0:
    print(" the length of the list is empty ")
else :
    print(" the length of the list is : ", y)

a = [1,2]
y = len(a)
if y==0:
    print(" the length of the list is empty ")
else :
    print(" the length of the list is : ", y)

# Write a Python program to clone or copy a list.
my__list = [1,2,3,4,5,6,7]
new__list = my__list.copy()
print(my__list)
print(new__list)
print(id(my__list))
print(id(new__list))

#original_list = [10, 22, 44, 23, 4]
#new_list = original_list[:]
#print(original_list)
#print(new_list)
#print(id(original_list))
#print(id(new_list))


# Write a Python program to find the list of words that are longer than n \n
# from a given list of words.

# write a python program to find the given number is prime or not:
#x = int(input(" enter a number : "))
#for i in range(2,x):
#    if x%i == 0 :
#        print(" the given number is not prime ")
#        break
#else:
#    print(" the prime number is : ", i)

# printing pattern's  :

#for i in range(4):
#    for j in range(4):
#        print("#",end="")
#    print()


#for i in range(4):
#    for j in range(i+1):
#        print("#",end="")
#    print()


#for i in range(4):
#    for j in range(4-i):
#        print("#",end="")
#    print()


#for i in range(4):
#    for j in range(1,5):
#        print(j,end="")
#    print()


#for i in range(4):
#    for j in range(i+1):
#        print(j,end="")
#    print()

# Write a Python function that takes two lists and returns True    \n
# if they have at least one common member.
#list1 =  [1,2,3,4,5,6]
#list2 =  [14,9,5,16,15]
#for x in list1:
#    for y in list2:
#        if x==y:
#            print(" True it has a common member :" ,y)
#            break
#        else:
#             print(" sorry there is no common number ")

#print()

#a =  [1,2,3,4,5,6]
#b =  [4,9,5,16,6]
#print([True for e in a if e in b])

#li=[2,3,4,5,6,7]
#li2=[4,5,6,8,9]
#print("true" if (len(set(li)&set(li2)))>0 else 'false')


#odd = [2, 4153, 5, 1, 2, 5, 7, 1]
#even = [2, 4, 6, 8]

#oddset = set(odd)
#evenset = set(even)
#if len(oddset.intersection(evenset)) > 0:
#    print(True)

# Write a Python program to print a specified list after removing , \n
# the 0th, 4th and 5th elements.
#x  = ["red","green","blue","white","pink","yellow"]
#x.pop(0)
#x.pop(3)
#x.pop(3)
#print(x)
#x.remove('red') \n #print(x)
#del x [0,4,5] \n #print(x)
#x.remove (0,4,5) \n #print(x)
#a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#print(a[1:4])
#sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#print(sample_list[1:4] + sample_list[6:])

#lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#for i in lst:
#    if lst.index(i) in (0,4,5):
#        continue
#    else:
#        print(i)

#                    pattrens
#for i in range(4):
#    for j in range(4):
#        print("#",end=" ")
#    print()

#for i in range(4):
#    for j in range(i+1):
#        print(j,end=" ")
#    print()

#for i in range(4):
#    for j in range(4-i):
#        print(j,end=" ")
#    print()

#for i in range(4):
#    for j in range(i+1):
#        print(j+1,end=" ")
#    print()
#for i in range(5):
#    for j in range(i+1):
#        print("*",end="")
#    print()

#for row in range(6):
#    for col in range(7):
#        if ((row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8) ):
#            print("*",end="")
#        else:
#            print(" ",end="")
#    print()

#x = int(input(" enter the number of rows : "))
#for i in range(1,x+1):
#    for j in range(i,x-1+1):
#        print(" ",end="")
#    for j in range(i,0,-1):
#        print(j,end="")
#    for j in range(2,i+1):
#        print(j,end="")
#    print()

#x = int(input("enter the number of rows : "))
#y = int(input("enter the number of col : "))

#for i in range(6):
#    for j in range(9):
#        if((i==0 and j==4)):
#            print("*",end="")
#        else:
#            print("",end="")
#    print()


# 13 Write a Python program to generate a 3*4*6 3D array whose each element is * ----->lists

# Write a Python program to print the \n
# numbers of a specified list after removing even numbers from it.

x = [8,10,7,17,19,55,25,30,0,56,100,101,125,199]
y = []
for i in x:
    if i%2==0:
        continue
    else:
        y.append(i)
print(y)


# Write a Python program to shuffle and print a specified list.

#from random import shuffle
#x = [9,4,6,14,16,5,6,7,8]
#print(shuffle(x))


#from random import shuffle
#x = [2,7,9,1,10,13,19,55,65,48]
#y = shuffle(x)
#print(y)


#from random import randint
#lst= []
#n= 10
#for x in range(n):
#    lst.append(randint(1,30))
#    print(lst)
# x = int(input(" enter the the number: "))
#lst = []
#for i in range(x):
#    if i%2==0:
#        continue
#    else:
#        lst.append(i)

#print(lst)


# Write a Python program to generate and print a list of first and last 5, \n
# elements where the values are square of numbers between 1 and 30 (both included).

#y = []
#for i in range(1,31):
#    if i<=5 or i>=26:
#        x = i**2
#        y.append(x)
#    else:
#        pass
#print(y)



def square():
    y = []
    for i in range(1,31):
        if i<=5 or i>=26:
            x = i**2
            y.append(x)

    print(y[:5],y[-5:])
square()

# Write a Python program to generate and print a list except for the first 5 elements,\n
# where the values are square of numbers between 1 and 30 (both included).
#y = []
#for i in range(1,31):
#    if i>5 :
#        x = pow(i,2)
#        y.append(x)
#print(y)

#def square():
#    y = []
#    for i in range(1,31):
#            y.append(i*i)
#    print(y[6:])
#square()

# print (i**2 for i in range(1, 30) if i >5)              #  it is not working

# write a python program to accept a filename from the user \n\t
# to print the extension of the file
#filename = input("enter the name of the of file  ")
#f = filename.split(".")
#print(" the extension of the file is " +repr(f[-1]))

# Write a Python program to generate all permutations of a list in Python.

# if i do  same program in interpreter it can works but here it is not working
#import itertools
#print(list(itertools.permutations([1,2,3])))

#import itertools
#user_input=input()
#lis=user_input.split()
#print(list(itertools.permutations(lis)))


# about split() function  -------> split() uses white spaces as a default separater.
# information gathered from real python.
x ='this is a string '
y = x.split()
print(y)
x ='this is a string '
y = x.split('s')
print(y)
record = '01027,ESTHAMPTON,MA'.split(',')
zip   = record[0]
city  = record[1]
state = record[2]
print(zip)
print(city)
print(state)
x ='  this is a string   '
y = x.split('s')
print(y)

x ='this is a string'
y = x.split(maxsplit=1)
print(y)

x ='this is a string'
y = x.split(',',maxsplit=1)
print(y)


# Write a Python program to get the difference between the two lists.
x = [2,5,7,9,10,12,11,15,48]
y = [11,22,5,6,9,150,100,96,78]
z = []
for i in x:
    for j in y:
       if i!=j:
        pass
       else:
        z.append(j)
print(z)

# it is working in interpreter but not here
#x = [2,5,7,9,10,12,11,15,48]
#y = [11,22,5,6,9,150,100,96,78]
#diff_x_y = list(set(x)-set(y))
#diff_y_x = list(set(y)-set(x))
#total_diff = diff_x_y + diff_y_x
#print(total_diff)


x = [2,5,7,9,10,12,11,15,48]
y = [11,22,5,6,9,150,100,96,78]
z = []
for i in x:
    if i not in y:
        z.append(i)
for i in y:
    if i not in x:
        z.append(i)
print(z)


# Write a Python program access the index of a list.
a = [1,2,3,4,5,6,7,8,9]
for i in a:
    print(i,a.index(i))
# print(enumerate(a)) it is working but not here.

# Write a Python program to convert a list of characters into a string.
a =['p','y','t','h','o',n]
b = ''.join(a)
print(b)

# If the list contains any non-string element,
#the above method does not work unless we use map() function to convert
# all elements to a string first.

L = ['L','O','L',1]
makeitastring = ''.join(map(str,L))
print(makeitastring)



test_list=["I","have",2,"numbers","and",8,"words","in","this","list"]
print(" ".join(map(str,test_list)))

list1=["j","a","v","a"]
a=""
for i in list1:
    a=a+i
print(a)

def convert(s):
    strg =''
    for i in s:
        strg = strg+str(i)
    return strg
print(convert([1,2,3,4,5,6,7,8]))
print(convert(["j","a","v","a"]))

# Write a Python program to find the index of an item in a specified list.
a = [1,2,3,4,5,6]
print(a.index(5))

# write a python program to flatten a shallow list.
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
d = a+b+c
print(d)


print(type(True))
x = 5
callable(x)
print(callable(x))

x = 10
y = 20
print(x == y)
print(x is y)

