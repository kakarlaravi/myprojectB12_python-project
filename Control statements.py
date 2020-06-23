# IF ELSE statement:
# {this code is executed but this is not efficient why because one if condition is right \n
# then there is no need  of evaluating the 2nd if condition.we can check it by using Debug.}
x = 8
r = x % 2
if r==0:
    print("The given number is even ");
if r==1:
    print("The given number is odd ");
# writing the code in efficient way, by using if else condtion,we can check it by Debug also.
x = 7
r = x % 2
if r==0:
    print("The given number is even ");
else  :
    print("The given number is odd ");

x = 12
r = x % 2
if r==0:
    print("The given number is even ");
else  :
    print("The given number is odd ");

# writing multiple if conditions in one program.
x = 16
r = x % 2
if r==0:
    print("The given number is even ");
    if x>5:
        print("the value of x is  Greater")
    else:
        print("the value of x is lesser")
else:
    print("The given number is odd ");
# writing a program using if,elif,else conditions.
x = "a"
if x=="b":
    print("the condtion of if is right ")
    print("thank u")
elif x=="z":
    print("the condition of elif is correct ")
    print("sorry if condition is wrong")
else :
    print("the condtion of else is right")
    print("the all above conditions are wrong that's why else is printing")
#

x = "a"
if x=="b":
    print("the condtion of if is right ")
    print("thank u")
elif x=="a":
    print("the condition of elif is correct ")
    print("sorry if condition is wrong")
else :
    print("the condtion of else is right")
    print("the all above conditions are wrong that's why else is printing")
#

x = "a"
if x=="a":
    print("the condtion of if is right ")
    print("thank u")
elif x=="z":
    print("the condition of elif is correct ")
    print("sorry if condition is wrong")
else :
    print("the condtion of else is right")
    print("the all above conditions are wrong that's why else is printing")

# while loop

i =1                        # initilization
while i<=5:                 # condition
    print("telsko")
    i = i+1                  # increment
else:
    print("done with the work")

i =5                       # initilization
while i>=1:                 # condition
    print("hello kakarla")
    i = i-1                  # decrement
else:
    print("done with the work")


# Nested while loop

i = 1
while i<=5:
    print("ravi",end ="")
    j = 1
    while j<=5 :
        print(" kakarla ",end ="")
        j =j+1
    i = i+1
    print()



#i = int(input(" enter a value "))
#while i<=5:
#    print("ravi",end ="")
#    j = 1
#    while j<=5 :
#        print(" kakarla ",end ="")
#        j =j+1
#    i = i+1
#    print()

# Short Hand If
a = 10
b = 8
if a > b : print(" a is greaterthan b ")

# Ternary Operators, or Conditional Expressions.

a = 100
b = 100
print(" a is lessthan b ") if a<b else (" a is greaterthan b ") if a>b else print(" a is equal to b ")

# for loop
#for x in range(10):
#    print(x)

#for i in range(1,10,1):
#    print(i)

#for i in range(1,10,2):
#    print(i)

# for i in range(20,1,-1):
#    print(i)
#i = ("ravindra ")
#for x in i:
#    print (x)
#i = ["ravindra ",123,143]
#for x in i:
#    print (x)
#for i in range(20,1,-1):
#    print(i)

for i  in range(1,20,1):
    if i%5!=0 :
        print(i)

# Break ,continue , Pass statements :
# Break
#available = 5
#x = int(input(" enter the number of candys u want : "))
#i = 1
#while i<=x:
#    if i>available:
#        print(" sorry there is no stock ")
#        break
#    print(" candy ")
#    i=i+1
#print(" Bye ")

# continue

# for i in range(1,101):
#    if i%3==0 or i%5==0 :
#        continue
#    print(i)

#print(" Bye ")


#for i in range(1,101):
#    if i%3==0 and i%5==0 :
#        continue
#    print(i)

#print(" Bye ")

#  pass
for i in range(1,101):
    if i%2!=0:
        pass
    else:
        print(i)
print(" bye ")


# for else :

i = [12,10,14,16,18,20,25]
for x in i:
    if x%5 == 0 :
        print(x)
        break
else:
    print("not found")

# printing prime numbers :-

#num = 59
#for i  in range(2,num):
#    if num%i==0:
#        print("The number is not prime number ")
#        break
#else:
#    print("The number is prime number ")


#for i in range(2,100):
#    if i%2==0 or i%3==0 or i%5==0 or i%11==0:
#        pass
#    else :
#        print(" The prime numbers are :",i)
#print()



#num = int(input(" enter the number : "))
#for i  in range(2,num):
#    if num%i==0:
#        print("The number is not prime number ")
#        break
#else:
#    print("The number is prime number ")


#for i in range(2, 100):
#    if i>1:
#        for j in range(2,i):
#            if i%j==0:
#              break
#        else:
#            print(i)


