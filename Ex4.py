# Exercise 4: Given a list and a value entered via the keyboard,
# determine whether the value exists in the list. If it does,
# return the index of its first occurrence

lst =[1,3,5,9,11,1,5,1,3,5,7]
print(len(lst))
print("List:",lst)
x = int(input("Input x: "))
position = -1
for i in range (0,len(lst)):
    if x==lst[i]:
        position = i
        break #Dừng lạiở vị trí đầu khi tìm thấy số
if position >=0:
    print("The position is: ",position)
else:
    print("Not found")