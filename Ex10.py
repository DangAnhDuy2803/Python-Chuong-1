# Exercise 10: Given a list, reverse the order of the elements
# and print the reversed list.
lst = [2,4,2,5,7,1,2,1,8,9,10,2,10,4,3,5]
print(lst)
newlst =[]
for i in range (len(lst)):
    newlst.insert(0,lst[i])
print(newlst)
