#  #2. count the occurrences of a particular element in the 
# #list and output highest occurring element
# days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]
# count_with_name = {}

days = ['sun','mon','mon','tue','wed','thu','fri','sat','mon','thu',]
count_with_name = {}
for day in days:
    if day not in count_with_name:
        count_with_name[day]=1
    else:
        count_with_name[day]+=1
        
highest_occurring_element=-1
for el in count_with_name:
    if count_with_name[el]>highest_occurring_element:
        highest_occurring_element=count_with_name[el]
print(count_with_name)        
print("highest_occurring_element:",highest_occurring_element)                    