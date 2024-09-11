# 3. Merge dictionaries a and b. The resultant dict must contain all items of 
# both dicts. If key is common then the value of key in resultant dict 
# must be the sum of value in a and b.
a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}
def Merge_dict(a, b):
  result = {}
  
  for elem in a:
    result[elem]= a[elem]
    
  for elem in b:
    if elem in result:
      result[elem] += b[elem]
    else:
      result[elem] = b[elem]
      
  return result
  
print(Merge_dict(a, b))