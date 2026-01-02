# Exercise 14: Given two lists, A and B,
# find and output their union (all unique elements combined).

lstA = [1,2,3,4,5,6,7,8,9]
lstB = [4,2,6,9,10,11,12,13,15,16]
lstC =[]
#ket hop lstA va lstB chi lay nhung gia tri ko giong nhau trong ca 2
# for x in lstA:
#     if x not in lstB:
#         lstC.append(x)
#
# for x in lstB:
#     if x not in lstA:
#         lstC.append(x)
# print(lstC)

#ket hop 2 lstA va lstB
for x in lstA:
    if x not in lstC:
        lstC.append(x)

for x in lstB:
    if x not in lstC:
        lstC.append(x)
print(lstC)