#   DICTIONARY
# Write a Python program to sort (ascending and descending) a dictionary by value.
#Original dictionary :  {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#Dictionary in ascending order by value :  {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
#Dictionary in descending order by value :  {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
from operator import itemgetter
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
print(d)
x = dict(sorted(d.items()))
print(" Asecending order of d is : ",x)
y = dict(sorted(d.items(),key=itemgetter(-1), reverse=True))
print(" discending order of d is : ",y)

