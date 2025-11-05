# Multification Pattern 
for i in range(1,6):
    for j in range(1,6):
        print(i * j , end="\t")
    print()     

# 34 prime Number checker 
n = int(input("Enter the num to check"))
def is_prime(n):
  if n <= 1:
    return False    
  for i in range(2, int(n**0.5) + 1):
     if n % i == 0:
        return False
  return True   

if is_prime(n):
   print(n,"Is prime num")
else:
   print(n, "is not a prime number")   

# 35 printt all prime number in range
def is_prime_num(n):
   if n <= 1:
      return False
   if n == 2 or n == 3:
      return True   
   if n % 2 == 0 or n % 3 == 0:
      return False
   
   i = 5
   while i * i <= n:
      if n % i == 0 or n % (i+2) == 0:
         return False
      i += 6
   return True  

start = int(input("Entert starting number: "))
end = int(input("Enter end of range: "))
print(f"Prime number between {start} and {end} are: ")

for num in range(start, end + 1):
   if is_prime(num):
      print(num, end=" ")


# armstrong Number checker
def is_armstrong(n):
   #count digits
   temp = n 
   digits= 0 
   while temp > 0:
      digits += 1
      temp //= 10

   # Sum of power of digits    
   temp = n
   total = 0
   while temp > 0:
      digit = temp % 10
      total += digit ** digits
      temp //= 10
   return total == n

num = int(input("Enter a number: "))
if is_armstrong(num):
   print(num,"Is an Armstrong number.")
else:
   print(num,"Is not an Armstrong Number")   

#37 Perfect Number checker
num = int(input("Enter a number: "))

sum_div = 0
for i in range(1,num):
   if num % i == 0:
      sum_div += i
if sum_div == num:
   print(num,"is a perfect Number") 
else:
   print(num, "is not a perfect number")   

# 38 Sum of digits
sum_dig = 0
while num > 0:
   digit = num % 10
   sum_dig += digit
   num //= 10

print("Sum of digits: ", sum_dig)

# 39 Reverse a number
original = num 
rev_num = 0

while num > 0:
   digit = num % 10 
   rev_num = rev_num * 10 + digit
   num //= 10
print("Reversed number: ", rev_num)   

num = int(input("Enter a number: "))

if num < 0:
   rev_num = -int(str(-num)[::-1])
else:
   rev_num = int(str(num)[::-1])

print("Reversed number: ", rev_num)

# Count of Even and Odd Digits in number
num = input("Enter a number: ")
num = str(abs(int(num)))

even = sum(1 for d in num if int(d) % 2 == 0)
odd = sum(1 for d in num if int(d) % 2 != 0)

print("Even didgits",even)
print("Odd digits", odd)