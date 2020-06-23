# once we start working on projects  thing is very very important
# so at this point u just remember function is a block where u will have one task
# so if u want to achive one task just write a functon for that its always a good
# practise to write function for separate tasks and we can call them  again
# infact there is one advantage u know in future if u want to modify something
# if u want modify  one code u can change only one function it will not affect other functions
# we can test  each function  individually  so its better to write functions.

def greet():
    print("hello")
    print("good morning")

greet()

# greet()       we can call this greet() as many times as we want

# adding two numbers and returning a value in functions.
#def add(a,b):  # a,b are arguments or parameters normally we can call it as a arguments.
#    c = a+b
#    print(c)
#add(5,4)

def add_sub(a,b):
    c = a + b
    d = a - b
    return c,d
result1,result2 = add_sub(5,4)
print(result1,result2)

def update(x):
    print(id(x)) # before updating x value the ids are same for both a and x.
    x = 8
    print("x",x)
    print(id(x))  # after updating the id's of x and and a are diffrenet.


a = 10
print(id(a))
update(a)        # when we call a function by passing a value we just pass a value not variable.
print(a)


def update(lst):
    print(id(lst))
    lst[1] = 40
    print("x",lst)
    print(id(lst))
# here in this case it is updating the origal lst as well as updated lst are same because
# it is mutable and the id's are same. (# 32,33,34,35 telusko by naveen.)
lst = [10,20,30]
print(id(lst))
update(lst)
print("lst",lst)

# Types  of arguments.

def add(a,b):  # formal argument's
    c = a+b
    print(c)
add(5,6)   # actual argument's this is divided into : positional,keyword,default,variable length



def add(a,b):
    c = a+b
    print(c)
add(5,6) #Here its mandotary for the programmer to follow the sequence  i.e positional argument's
# if we are not followig the sequence also there is one more way i.e introducing  keyword's.
def person(name,age):
    print(name)
    print(age)
person(age=23,name='ravi')    # here introducing the age,name are keword argument's.

def person(name,age=18):# Here the age is the default argument's.
                     # if we mention the age while at the time of calling the function
                     # the default value will ger earsed.
    print(name)
    print(age)
person('ravi')


def add(a,*b):    # variable length i.e a is string and b is tuple.
    print(a)
    print(b)
    c = a
    for i in b:
        c = c+i
    print(c)
add(5,6,7,98,102)


# keyword variable length argument nothing **kwargs
def person(name,**data):  # when want to send multiple data by using keywords we mention **
    print(name)
    print(data)
    for i,j in data.items():
        print(i,j)
person("ravi",age=23,city='bengaluru',mob=9652257724)

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#  to let a function return value ,use return statement.

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

def sayhello(name):
    print(" Hello.."+name+" welcome to function's concept in python ")
sayhello("ravi")

def sayhello(name="kakarla ravi"):
    print(" Hello.."+name+" welcome to function's concept in python ")
sayhello(name = " kakrla")

def sayhello(name):
    print(" Hello.."+str(name)+" welcome to function's concept in python ")
sayhello(10)



a = {1,2,3,}
b=a
print(id(a))
print(id(b))


x = [1,2]
y = [1,2]
print(x==y)
print(x is y)
print(id(y))
print(id(x))

