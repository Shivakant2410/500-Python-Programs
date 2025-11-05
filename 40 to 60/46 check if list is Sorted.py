l = [1,2,32,14,54,2,5,6,3]

for i in range(len(l)-1):
    if l[i] > l[i+1]:
        break
print("check mixture of  "if l is sorted else "not Sorted")    

# Ascending 
arr = [1, 2, 3, 4, 5]
is_sorted = True

for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break

print("Ascending Sorted:" if is_sorted else "Not Sorted")

# descending list
arr = [5,2,4,3,2,1]
is_sort = True
for i in range(len(arr)-1):
    if arr[i] < arr[i+1]:
        is_sort = False
        break
print("Descending Sorted: " if is_sort else "Not Sorted")   