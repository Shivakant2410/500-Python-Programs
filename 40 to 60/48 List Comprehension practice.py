# List comprehension practice

def squ_even(lst):
    result = []
    for num in lst:
        if num % 2 == 0:
            result.append(num ** 2)
    return result



# Optimized 
def squ_opti(lst1):
    return [num ** 2 for num in lst1 if num % 2 == 0]


#Recursive Approach

def squa_even_rec(lst2):
    if not lst2:
        return []
    first, rest = lst2[0], lst2[1:]
    if first % 2 == 0:
        return [first ** 2] + squa_even_rec(rest)
    else:
        return squa_even_rec(rest)
    

lst = [1, 2, 3, 4, 5, 6]
print(squa_even_rec(lst))