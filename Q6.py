#duplicates value

string_list = ["Empathy", "Empathy", "Kindness", "Kindness", "Compassion", 
"Humble", "Humble"]
newlist=[]
for i in string_list:
    if i not in newlist:
        newlist.append(i)
print(newlist)