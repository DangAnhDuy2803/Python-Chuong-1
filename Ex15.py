# Exercise 15: Given a list, count and display
# the number of occurrences of each value in the list.

lstA = [1,3,5,1,2,4,5,6,7,8,2,7,6,5,8,9,3]
lstB =[]
lstC =[]

for x in lstA:
    if x not in lstB:
        count = 0
        for y in lstA:
            if x == y:
                count += 1
        lstB.append(x)
        lstC.append(count)

print(lstB)
print(lstC)
