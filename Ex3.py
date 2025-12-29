#Exercise 3: Given a list and a value entered via the keyboard,
# determine whether the value exists in the list.

lst = [1,4,6,8,9,6,10,12,20,26,35,36,25]
x = int(input("Input x: "))
if x in lst:
    print("Exist")
else:
    print("Not Exist")