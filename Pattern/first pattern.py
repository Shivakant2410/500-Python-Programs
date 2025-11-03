
'''for i in range(5):
    print("*")

for i in range(5):
    print("*",end="")
'''
for i in range(5):
    for j in range(0,i+1):
        print("*",end="")
    print()        
#31 Print start pattern 
# for triangle Pattern
n = 5 
for i  in range(0,n+1):
    for j in range(0,i+1):
        print("*",end =" ")
    print(" ")    
# reverse triangle
n = 5
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=' ')
    print()    

#Pyramid pattern 
n = 5
for i in range(1,n+1):
        print(" " * (n -i) + "*" * (2 * i - 1))

for i in range(n -2, -1 ,-1):
     print(" " * (n - i - 1) + "*" * (2 *i +1))
     
#Diamond
n = 5 

for i in range(n):
     print(" " * (n - i - 1) + "*" * (2 * i +1))

for i in range(n - 2, -1, -1):
     print(" " * (n -i -1) + "*" * (2* i + 1))     

## hollow diamond pattern   
for i in range(n):
     print(" "* (n-i-1), end="")
     for j in range(2 * i + 1):
          if j == 0 or j == 2* i:
               print("*", end ="")
          else:
               print(" ",end="")
     print()          

#lowehalf
for i in range(n - 2, -1, -1):
     print(" " * (n - i - 1), end="")
     for j in range(2 * i + 1):
          if j == 0 or j == 2 *i:
               print("*", end="")
          else:
               print(" ", end="")
     print()               

 ## Butterfly Pattern

for i in range(1, n + 1):
     print("*" * (i ) + " " *(2 * (n -i)) + "*" * i)

for i in range(n,0,-1):
     print("*" * i + " " * (2 *(n -i)) + "*" * i)     

# Hollow Pyramid

for i in range(n):
     print(" " * ( n- i -1), end="")
     for j in range(2 * i + 1):
          if j == 0 or j == 2*i or i == n -1:
               print("*",end="")
          else:
               print(" ", end="")
     print()               