# Exercise 13: Given two lists, A and B,
# find and output their intersection (common elements).

lstA = [1,2,3,4,5,6,7,8,9]
lstB = [4,2,6,9,10,11,12,13,15,16]
lstC =[]

for x in lstA:
    if x in lstB:
        if x not in lstC:
            lstC.append(x)
print(lstC)

