# Exercise 9: Given a list, create and output a set containing only the unique
# (non-repeating) elements of the list.
lst = [2,4,2,5,7,1,2,1,8,9,10,2,10,4,3,5]
print(lst)
reducedlst=[] #Create an empty list
for i in range (0,len(lst)):
    if lst[i] not in reducedlst:
        reducedlst.append(lst[i])
print(reducedlst)

