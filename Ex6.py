# Exercise 6: Given a list and a value entered via the keyboard,
# count the number of times the value appears in the list.
lst = [1,2,3,4,2,3,6,7,8,1,9,2,4]
x = int(input("Input x: "))
numberofOccurence = 0
for i in range (0,len(lst)):
    if x == lst[i]:
        numberofOccurence += 1

if numberofOccurence >0:
    print(x, " exists in list ", numberofOccurence, " times")
else:
    print(x, "doesn't exist")