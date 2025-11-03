# String && Loops

# 21 Counting Vowels and consonants in a string

str1 = input("Enter a string to count: ").lower()
count = 0
consonants = 0
for ch in str1:
   if ch.isalpha(): 
    if ch in "aeiou":
        count += 1
    else:
        consonants += 1     

print(count)
print(consonants)

#22 Reverse a String
str2 = "HELLO"

print(str2[::-1])

#| 23 | Check for Anagram                      |
str3 = "listen"
str4 = "silent"
str3 = str3.replace(" ","").lower()
str4 = str4.replace(" ","").lower()
if sorted(str3) == sorted(str4):
    print("They are anagrams!")
else:
    print("They are not anagrams.")
#| 24 | Character Frequency in String          |
s = "banana"
freq = {ch: s.count(ch) for ch in set(s)}
mo_co = max(freq, key = freq.get) #it’s a type-checking warning
print(mo_co)
#| 25 | Remove Punctuation from String         |
ss = "Hello! ,How ,are you,?"
punctuation = "!\"#$%&'()*+,-./:;<=>?[\\]^_`{|}~"
clean_text = ""
for ch in ss:
   if ch not in punctuation:
      clean_text += ch
print(clean_text)      