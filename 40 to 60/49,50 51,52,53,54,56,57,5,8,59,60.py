"""#49 Tuple to list and list to Tuple Conversion
t = (1,2,3)
lst = [4,5,6]

# Tuple to list
def tup_to_list(t):
    return list(t)

# List tot uple
def list_to_tuple(lst):
    return tuple(lst)

print(tup_to_list(t))
print(list_to_tuple(lst))

a = 5
b = 10
# 50 Unpack Tuple
def swap_rec(a,b,depth=0):
    if depth == 1:
        return b,a
    return swap_rec(a,b,depth+1)

print(swap_rec(a,b))

# 51 Dictionary Key existence check
fruits = {"apple":1,"Banana":3,"orange":2}
if "Banana" in fruits:
    print("Banana is available!")
else:
    print("Banana is not available.")    
#Checking multiple keys

keys_to_check = ["apple","Banana"]
for key in keys_to_check:
    if key in fruits:
        print(f"{key} is available")
    else:
        print(f"{key} is not available")    


 # 52 merge two dictionary 
dict1 = { "apple":2,"Banana":1}
dict2 = {"Mango":4,"Orange":3}

dict1.update(dict2)
print(dict1)

 # 53 Sort Dictionary by value

sort_fruit = dict(sorted(dict1.items(), key=lambda itme: itme[1]))
print(sort_fruit)
"""
 # 54 frequency of Elements in Dictionary
fruit_list = ["apple","apple","apple","Orange","banana","banana","banana","Orange","Mango"]
frequency = {}
for fruit in fruit_list:
    if fruit in frequency:       
        frequency[fruit] += 1
    else:
        frequency[fruit] = 1
print(frequency)            

 # 55 Remove Key from Dictionary

fruit_list.remove("banana")
print(fruit_list)

# 56 iterate through dictionary
for fruit in fruit_list:
    print(fruit)

# 57 | Create Dictionary from Two Lists        
lst = ["Mango","apple","Orange"]
key = [1,2,3]
fruit_lis = dict(zip(lst,key))
print(fruit_lis)

# 58 | Nested Dictionary Access       
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 21, "grade": "A"}
}

print(students["Alice"])
print(students["Bob"]["age"])
# 59 | Minimum and Maximum in Dictionary    
min_fruit = min(fruit_lis.items(),key=lambda x: x[1])
print(min_fruit)

# 60 | Dictionary comprehension Practice
num = [1,2,3,4,5,6,7]
squares = {nums:nums **2 for nums in num }
print(squares)