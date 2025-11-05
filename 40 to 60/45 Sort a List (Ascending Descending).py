list1 = [1,2,3,34,56,6]

# NOrmal approah\ch Using Loops/ Basic Sorting
n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j] > list1[j+1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]

print("Ascending:", list1)       

n = len(list1)
for i in range(n):
    for j in range(0,n-i-1):
        if list1[j] < list1[j+1]:
            list1[j], list1[j+1] = list1[j + 1], list1[j]

print("Descending: ", list1)


# Optimal Approach Using Built in Sort/ Efficient Algorithm

arr = [5,2,36,74,4,2,9,8,0,4,3,2]

asc = sorted(arr)
print("Ascending: ", asc)

desc = sorted(arr, reverse = True)
print("Descending", desc)

# Recursive Approach using Bubble Sort
def rec_sort(arr, n =None):
    if n is None:
        n = len(arr)
    if n == 1:
        return

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    rec_sort(arr, n-1)

print("Ascendning (Recurse)", arr) 

#most optimal approach
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

arr = [5, 2, 9, 1, 5, 6]
asc = merge_sort(arr)
desc = merge_sort(arr)[::-1]  # Reverse for descending
print("Ascending (Recursive Merge Sort):", asc)
print("Descending (Recursive Merge Sort):", desc)
