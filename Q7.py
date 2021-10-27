#duplicate value

list1 = [1, 342, 75, 23, 98]

list2 = [75, 23, 98, 12, 78, 10, 1]
newlist=[]
for i  in range(len (list2)):
    j=0
    while j<(len(list1)):

        if list2[i]==list1[j]:

           newlist.append(list2[i])
        j+=1
print(newlist)
