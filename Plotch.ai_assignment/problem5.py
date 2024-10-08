 #5. Implement a group_by_owners function that:
#Accepts a dictionary containing the file owner name for each file name.
#Returns a dictionary containing a list of file names for each owner #name, in any order.
#files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
#the group_by_owners function should return 
# output = {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.


def group_by_owners(files):
    ans = {}
    for file, owner in files.items():
        if owner in ans:
            ans[owner].append(file)
        else:
            ans[owner] = [file]
    return ans


files = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} 
output = group_by_owners(files)
print(output)
