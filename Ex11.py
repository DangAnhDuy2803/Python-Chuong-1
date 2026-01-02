# Exercise 11: Given a list of numbers, sort the elements in ascending order.

lst = [2,4,2,5,7,1,2,1,8,9,10,2,10,4,3,5]
print(len(lst))
print("List: ",lst)
for i in range (0, len(lst)-1):
    print("Step: ",i)

    for j in range (i+1, len(lst)):
        if lst[i] > lst[j]:
            temp = lst[i]
            lst[i] = lst[j]
            lst[j] = temp
            print("Change: ", lst)
print("List after sorting: ",lst)

