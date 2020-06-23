x = 10
print(type(x))
x = 'ravi'
print(type(x))
x = 2+3j
print(type(x))
x = 10>9
print(type(x))

x = ['ravi','kakarla','anathapuram']
print(type(x))

x = ('ravi','kakarla','anathapuram')
print(type(x))

x = {'ravi','kakarla','anathapuram'}
print(type(x))

x = {'ravi': 10,'kakarla': 15,'anathapuram': 20}
print(type(x))


x = 5.6
y = int(x)
print(type(y))
print(y)
print(float(y))

y = 10
z = complex (x,y)
print(z)

c= x<y
print(c)

d= x>y
print(d)
print(type(d))


x = range(10)
print(x)

x = list(range(10))
print(x)

x = list(range(2,10,2))
print(x)


x = {"ravi": 10 , "kakarla": 20 ,"anathapuram": 30}
print(type(x))
print(x.keys())
print(x.values())
print(x['kakarla'])
print(x.get('ravi'))



txt = " Hello World "
x = txt.strip()
print(x)


txt = "Hello world"
x= txt.upper()
print(x)


age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))


Thisset = {'banana','ravi','kakarla','chowdary'}
x = Thisset.pop()
print(x)
print(Thisset)




thislist = ['ravi','kakarla','chowdary','ananthapuram','sarada nagar','sai college']
print(thislist)
#printing 2nd item in the list
print(thislist[1])
#printing last item in thislist
print(thislist[5])
#printing range of indexing from where to start and where to end
print(thislist[2:6])
#printing from start to middle
print(thislist[:5])
print(thislist[1:])
print(thislist[:len(thislist)])

#negative indexing
print(thislist[-4:-1])
#replacing
thislist[0] = 'ravindra'
#for x in thislist
print(thislist)
print(len(thislist))

# using append method
thislist.append('btech')
print(thislist)

# using insert method
thislist.insert(5,'ananthalaxmi engineering college')
print(thislist)

# removing an item from list
thislist.remove('sai college')
print(thislist)

#using pop() method
thislist.pop()
print(thislist)

# using max and minimum keywords

x = 'ravi'
#max(x)
print(max(x))

x1 = "kakarla"
print(max(x1))


x = 'ravi'
print(min(x))

x1 = "kakarla"
print(min(x1))

#y = 'ravi'
#print(y.upper('ravi'))


# aceesing indexing values to string

var1 = "hello world "
var2 = " python programming "
print("var1 [0] : ", var1[0])
print("var2[1:5]:", var2[1:5])

# updating string
var1 = "hello world"
print ("updating strings:-", var1[:6]+'python')

#	Accessing values in Lists:
list1 =['physics','chemistry',1997,2000]
print("list1[0]:",list1[0])
list2 =[1,2,3,4,5,6,7];
print("list2[1:5]:",list2[1:5])

# Updating values in Lists
list =['physics','chemistry',1997,2000]
print (" value available at index 2 is :")
print (list[2])
list[2] = 2001
print (" value updated  at index 2 is ")
print(list[2])


#  Delete List Elements in Lists:

list =['physics','chemistry',1997,2000]
print('Before deleting the index 2 value in list')
print(list)
del list[2]
print('after deleting the index 2 value  in list ')
print(list)

# tuples
#Accessing Values in Tuples:
tup3 = "a", "b", "c", "d";
print(tup3)

tup1 =('physics','chemistry',1997,2000);
print("tup1[0]: ", tup1[0])
tup2 =(1,2,3,4,5,6,7);
print("tup2[1:5]: ", tup2[1:5])

tup1 =(12,34.56);
tup2 =('abc','xyz');
# Following action is not valid for tuples
# tup1[0] = 100;
# So let's create a new tuple as follows
tup3 = tup1 + tup2;
print (tup3)

tup =('physics','chemistry',1997,2000);
print (tup)
del tup;
#print"After deleting tup : ";
# print (tup)

# Dictionary's
# Acessing the values in dictionary

dict  = {'Name':'Zara',
         'Age':7,
         'Class':'First'
        }
print ("dict['Name']:", dict['Name'])
print ("dict['Age']:", dict['Age'])


# updating dictionary

dict ={'Name':'Zara','Age':7,'Class':'First'}
print(dict)
dict['Age'] = 8
print('dict[Age]:','dict[Age]')
dict['school'] = "zph school"
print(dict)


# Delete Dictionary Elements:
dict ={'Name':'Zara','Age':7,'Class':'First'}
del dict['Name'];# remove entry with key 'Name'
dict.clear();# remove all entries in dict
del dict ;# delete entire dictionary

#print("dict['Age']: ", dict['Age'])
#print("dict['School']: ", dict['School'])


num = 10
print(id(num))

a = 10
b = 10
print(id(a))
print(id(b))


num = [1,2,6,5,8,10]
print(num)

b = 10
c = 20
k = b<c
print(k)
print(type(k))


# to convert list into dictonary

keys   = ['ravi','teja','dharani','bheema']
values = ['python','java','selenium','data science']
data   = dict(zip(keys,values))
print(data)

prog = {'js':'Atom','cs':'vs','python':['pycharm','sublime'],'java':{'js':'Netbeans','Jee':'eclipse'}}
print(prog)

print(prog ['js'])
print(prog['python'])
print(prog['python'][1])
print(prog['java']['Jee'])
# print(prog['java'] ['keys'])

nums   = [25,12,36,95,14]
names  = ['navin','kiran','john']
mil  = [nums,names]
print(mil)

nums.extend([88,55,65,75,89])
print(nums)
del nums[1]
print(nums)
print(max(nums))
print(min(nums))
print(sum(nums))
print(nums.pop(5))
print(nums.pop())
print(nums.sort())

# variable is the container where we can store our value.or
# variable is a container where we can put our values.
x = 10
y = 20
z = x+y
print(z)
# c = _+ y ('_' , underscore is used to represent the output of the previous operation )
print(x+y)
print(x+58)
#print(_+58)

x = 'ravidra'
print(x +" chowdary"+" kakarla")


x = " ravindra chowdary kakarla "
print(x[::])
print(x[:])

x = [1,2,3,4,5]
print(x[1])
print(x[::])
# print(x[:,:-])

print(len(x))
#"Twinkle, twinkle, little star, How I wonder what you are! " \
#"Up above the world so high, Like a diamond in the sky. " \
#"Twinkle, twinkle, little star, How I wonder what you are!"
# printing enlglish paragraph
print("Twinkle,twinkle,little star, "
      "\n\tHow I wonder what you are! "
      "\n\t\tUp above the world so high "
      "\n\t\tLike a diamond in the sky."
      "\nTwinkle,twinkle,little star,"
      "\n\tHow I wonder what you are!")
#print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# Write a Python program to get the Python version you are using.
import sys
print("python version")
print(sys.version)
print("python version_info.")
print(sys.version_info)

#import sys
#a = sys.version
#b = sys.version_info
#print("The phyton vesion is " + str(a) + "\nThe version info is - " + str(b))

import datetime
print("current date and time is")
#print(datetime.datetime.now())   # possible case
#now = datetime.datetime.now()
#print (now.strftime("%Y-%m-%d %H:%M:%S"))  # possible case
#print(now)

import time
print(time.ctime())

# write a program which accepts the radius of circle from user and  compute the area
#from math import pi
#r = float(input("input radius of the circle : 20 "))
#print(r)

from math import pi
r = float(input ("Input the radius of the circle :  20 "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


x = ("ravi","kakarla")
print(list(x))

x = ["ravi","kakarla"]
print(tuple(x))
x = ['ravi','kakarla']
print(set(x))
#x = ['ravi','kakarla']
#print(dict("x[0]:1,x[1]:2"))

