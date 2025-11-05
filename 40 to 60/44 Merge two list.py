# merge two list 

list1 = [1,2,3,4,5,6]
list2 = [7,8,9,0,12,3,4]

def merge_lst(lst, lst2):
    result = []

    for item in list1:
        result.append(item)
    for item in list2:
        result.append(item)
    return result
        
print("merge list ",merge_lst(list1, list2))

# Most optimal Approach to Merge list 

def merge_list_optimal(lst1,lst2):
    return lst1 + lst2

# Recursive Approach 

def merge_list(list1, list2):
    if not list1:
        return list2
    return [list1[0]] + merge_list(list1[1:], list2) 

lit1 = [1,2,3]
lit2 = [2,3,4,5]
print(merge_list(lit1,lit2))

