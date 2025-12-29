# Exercise 2: Given a list of numbers, calculate the average, maximum,
# and minimum values of the elements in the list.

from numpy import average

lst = [5,10,15,20,25,30,35]
avg = average(lst)
print(avg)

maxvalue = max(lst)
print(maxvalue)

minvalue = min(lst)
print(minvalue)
