list1 = [1,2,3,4,4,5,4,4,4,4,3,2,4,4,5,9,8,7,9,8,7]
#sorting 
uni_arr = list(set(list1))
uni_arr.sort()
print(uni_arr)

#Normal iterative Approach to remove duplicates
def rem_dup_iter(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

print(rem_dup_iter(list1))

#Most Optimal Sol using a Set
List2 = [1,2,1,2,1,1,2,3,3,4,2]

def remove_dup(lst):
    seen = set()
    result = []
    for item in lst:
      if item not in seen:  
        seen.add(item)
        result.append(item)
    return result
print(remove_dup(List2))

# Recursive Approach 
def remo_rec(lst, seen = None):
   if seen is None:
      seen = set()
   if not lst:
      return []
   first, rest = lst[0], lst[1:]

   if first in seen:
      return remo_rec(rest,seen) 
   else:
      seen.add(first)
      return [first] + remo_rec(rest,seen)

print(remo_rec(list1))      