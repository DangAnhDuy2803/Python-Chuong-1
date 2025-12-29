# Exercise 4: Given a list and a value entered via the keyboard,
# determine whether the value exists in the list. If it does,
# return the index of its first occurrence

lst =[1,2,3,4,5,6,2,8,4,3,6,5,6,5,7,8,9]
print(len(lst))
print("List: ",lst)
x = int(input("Input x: "))
position = -1
for i in range(0,len(lst)):
    if x==lst[i]:
        position = i

if position >=0:
    print("Last position at ",i+1)
else:
    print("Not Found")