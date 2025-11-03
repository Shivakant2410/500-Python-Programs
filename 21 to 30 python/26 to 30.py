#| 26 | Capitalize Each Word                   |
ss = "hello, i am shiva 2233"
print(ss.title())
#| 27 | Count Digits and Letters               |
letter = 0
digits = 0

for ch in ss:
    if ('A' <= ch <= 'Z') or ('a'<= ch <='z'):
        letter += 1
    elif '0' <= ch <= '9':
        digits += 1

print(digits)
print(letter)
#| 28 | Replace Substring                      |
print(ss.replace("Hello","Borrow",1))
#| 29 | Count Words in Sentence                |

ss = "Hello! my dshiva"
ss1 = len(ss.split())
print(ss1)
#| 30 | Find Longest Word                      |
ss2 = ss.split()
#longest = max(ss2, key=len)
max_len = max(len(ss3) for ss3 in ss2)
longes = [ss3 for ss3 in ss2 if len(ss3) == max_len]
print(longes)