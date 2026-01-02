# Exercise 8: Given a list and a value entered via the keyboard,
# remove all instances of the value from the list.

lst = [1,3,2,4,2,5,6,9,7,8,8,8,9,8,7]
print(lst)
x = int(input("Input x: "))
while x in lst:
    lst.remove(x)
print(lst)