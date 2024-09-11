#   #4. Return the Item with highest value count
#items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}] 
# #Output: Mumbai


def highest_count(items):
    highest_value_count=-1
    for item in items:
        city=""
        count=0
        for el in item:
            city=el
            count=item[el]
        if count>highest_value_count:
            highest_value_count=count
    return highest_value_count        

items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}]
print("highest_value_count:",highest_count(items))


