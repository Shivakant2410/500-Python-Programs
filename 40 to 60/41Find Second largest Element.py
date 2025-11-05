# Find second Largest Element
# let's first try basic approach SORITNG
arr = [1234,2,323,34,5,56,36]
# remove duplicates and sort the array 
unique_arr = list(set(arr))
unique_arr.sort()

if len(unique_arr) < 2:
    print("no second largest element.")
else:
    print("Second largest element:", unique_arr[-2])


# Optimal Approach (Single Pass, O(n))

if len(arr) < 2:
    print("No second largest element") 
else:
    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif first > num > second:
            second = num
    if second == float('-inf'):
        print("No second largest element")
    else:
        print("Second largest element:", second)    