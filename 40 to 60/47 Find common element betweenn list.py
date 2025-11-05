# Find Common element between List

list2 = [3,4,2,5,3,5,6,7,8]
list1 = [2,3,4,5,3,4,5,6]

# Normal approach 
common = []
for item in list2:
    if item in list1:
        common.append(item)
print("Common element: ", common)

# optimized Approach

common = list(set(list2) & set(list1))
print("Common elements: ", common)

#Recursive 
def comm_ele_rec(list3, list4):
    if not list3:
        return []
    first =list3[0]
    rest = comm_ele_rec(list3[1:], list4)
    if first in list4 and first not in rest:
        return [first] + rest
    else:
        return rest
        
l = [1,2,3,4,5,6,7]
l1 = [4,5,6,7,8,9]
print(comm_ele_rec(l,l1))        