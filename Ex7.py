# Exercise 7: Given a list and a value entered via the keyboard,
# if the value exists in the list, remove the element at its first occurrence.

lst = [1,2,3,4,2,3,6,7,8,1,9,2,4]
print(lst)
x = int(input("Input x: "))
for i in range(0,len(lst)):
    if x==lst[i] :
        lst.pop(i) #remove at i
        break
print(lst)